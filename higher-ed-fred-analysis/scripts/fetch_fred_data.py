#!/usr/bin/env python3
"""
FRED Data Fetcher for Higher Education Economic Analysis

Fetches economic data from the Federal Reserve Economic Data (FRED) API
with error handling, caching, and output formatting.

Usage:
    python fetch_fred_data.py --series SLOAS LNS14027662 --api-key YOUR_KEY
    python fetch_fred_data.py --series SLOAS --api-key YOUR_KEY --output data.json
    python fetch_fred_data.py --config config.json
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import urllib.request
import urllib.error
import urllib.parse


class FREDFetcher:
    """Fetch data from FRED API with error handling and caching."""
    
    BASE_URL = "https://api.stlouisfed.org/fred/series/observations"
    
    def __init__(self, api_key: str, cache_dir: Optional[Path] = None):
        self.api_key = api_key
        self.cache_dir = cache_dir or Path(".fred_cache")
        self.cache_dir.mkdir(exist_ok=True)
        
    def fetch_series(
        self, 
        series_id: str,
        limit: int = 1000,
        sort_order: str = "asc",
        observation_start: Optional[str] = None,
        observation_end: Optional[str] = None
    ) -> Dict:
        """
        Fetch a single FRED series.
        
        Args:
            series_id: FRED series ID (e.g., 'SLOAS', 'LNS14027662')
            limit: Maximum number of observations to return
            sort_order: 'asc' or 'desc'
            observation_start: Start date in YYYY-MM-DD format
            observation_end: End date in YYYY-MM-DD format
            
        Returns:
            Dict containing series metadata and observations
        """
        # Build query parameters
        params = {
            'series_id': series_id,
            'api_key': self.api_key,
            'file_type': 'json',
            'sort_order': sort_order,
            'limit': str(limit)
        }
        
        if observation_start:
            params['observation_start'] = observation_start
        if observation_end:
            params['observation_end'] = observation_end
            
        # Check cache
        cache_file = self._get_cache_path(series_id, params)
        if cache_file.exists():
            print(f"Loading {series_id} from cache...", file=sys.stderr)
            with open(cache_file, 'r') as f:
                return json.load(f)
        
        # Fetch from API
        print(f"Fetching {series_id} from FRED API...", file=sys.stderr)
        url = f"{self.BASE_URL}?{urllib.parse.urlencode(params)}"
        
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                data = json.loads(response.read().decode())
                
            # Check for API errors
            if 'error_code' in data:
                raise ValueError(f"FRED API error: {data.get('error_message', 'Unknown error')}")
            
            # Process observations
            observations = data.get('observations', [])
            
            # Filter out missing data markers (".")
            valid_obs = [
                obs for obs in observations 
                if obs['value'] != '.'
            ]
            
            result = {
                'series_id': series_id,
                'retrieved_at': datetime.now().isoformat(),
                'count': len(valid_obs),
                'observations': valid_obs
            }
            
            # Cache the result
            with open(cache_file, 'w') as f:
                json.dump(result, f, indent=2)
                
            return result
            
        except urllib.error.HTTPError as e:
            raise ValueError(f"HTTP error fetching {series_id}: {e.code} {e.reason}")
        except urllib.error.URLError as e:
            raise ValueError(f"Network error fetching {series_id}: {e.reason}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON response for {series_id}")
    
    def fetch_multiple(self, series_ids: List[str], **kwargs) -> Dict[str, Dict]:
        """
        Fetch multiple FRED series.
        
        Args:
            series_ids: List of FRED series IDs
            **kwargs: Additional arguments passed to fetch_series
            
        Returns:
            Dict mapping series_id to series data
        """
        results = {}
        errors = {}
        
        for series_id in series_ids:
            try:
                results[series_id] = self.fetch_series(series_id, **kwargs)
            except Exception as e:
                errors[series_id] = str(e)
                print(f"Error fetching {series_id}: {e}", file=sys.stderr)
        
        if errors:
            print(f"\nWarning: Failed to fetch {len(errors)} series", file=sys.stderr)
            
        return results
    
    def _get_cache_path(self, series_id: str, params: Dict) -> Path:
        """Generate cache file path based on series and parameters."""
        # Create a simple cache key from series ID and key params
        cache_key = f"{series_id}_{params.get('limit', '1000')}_{params.get('sort_order', 'asc')}"
        return self.cache_dir / f"{cache_key}.json"
    
    def clear_cache(self, series_id: Optional[str] = None):
        """Clear cached data for specific series or all series."""
        if series_id:
            for cache_file in self.cache_dir.glob(f"{series_id}_*.json"):
                cache_file.unlink()
                print(f"Cleared cache for {series_id}", file=sys.stderr)
        else:
            for cache_file in self.cache_dir.glob("*.json"):
                cache_file.unlink()
            print("Cleared all cached data", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch economic data from FRED API for higher education analysis"
    )
    parser.add_argument(
        '--series',
        nargs='+',
        help='FRED series IDs to fetch (e.g., SLOAS LNS14027662)'
    )
    parser.add_argument(
        '--api-key',
        help='FRED API key (or set FRED_API_KEY environment variable)'
    )
    parser.add_argument(
        '--config',
        help='JSON config file with series list and parameters'
    )
    parser.add_argument(
        '--output',
        default='fred_data.json',
        help='Output file path (default: fred_data.json)'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=1000,
        help='Maximum observations per series (default: 1000)'
    )
    parser.add_argument(
        '--clear-cache',
        action='store_true',
        help='Clear cached data before fetching'
    )
    parser.add_argument(
        '--no-cache',
        action='store_true',
        help='Disable caching (always fetch fresh)'
    )
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key
    if not api_key:
        import os
        api_key = os.environ.get('FRED_API_KEY')
    
    if not api_key:
        print("Error: API key required. Use --api-key or set FRED_API_KEY environment variable.", 
              file=sys.stderr)
        sys.exit(1)
    
    # Initialize fetcher
    cache_dir = None if args.no_cache else Path(".fred_cache")
    fetcher = FREDFetcher(api_key, cache_dir)
    
    # Clear cache if requested
    if args.clear_cache:
        fetcher.clear_cache()
    
    # Determine series to fetch
    series_ids = []
    if args.config:
        with open(args.config, 'r') as f:
            config = json.load(f)
            series_ids = config.get('series', [])
    elif args.series:
        series_ids = args.series
    else:
        print("Error: Either --series or --config must be provided", file=sys.stderr)
        sys.exit(1)
    
    # Fetch data
    print(f"Fetching {len(series_ids)} series from FRED...\n", file=sys.stderr)
    results = fetcher.fetch_multiple(series_ids, limit=args.limit)
    
    # Write output
    output_path = Path(args.output)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nSuccessfully fetched {len(results)} series", file=sys.stderr)
    print(f"Output written to: {output_path}", file=sys.stderr)
    
    # Print summary
    print("\nSummary:", file=sys.stderr)
    for series_id, data in results.items():
        count = data.get('count', 0)
        print(f"  {series_id}: {count} observations", file=sys.stderr)


if __name__ == '__main__':
    main()
