from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange
from google.oauth2.credentials import Credentials
from datetime import date, timedelta
import re
import yaml


def get_page_views(property_id):
    """
    Retrieve page views for pages with paths starting with '/YYYY' in the specified GA4 property 
    for the last 6 months and write to YAML.
    """
    
    # Initialize the GA4 client
    # Note: You need to set up authentication separately
    client = BetaAnalyticsDataClient(credentials=Credentials.from_authorized_user_file('path/to/your/credentials.json'))

    # Calculate date range for the last 6 months
    end_date = date.today()
    start_date = end_date - timedelta(days=180)  # Approximately 6 months

    # Configure the report request
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[{"name": "pagePath"}],
        metrics=[{"name": "screenPageViews"}],
        date_ranges=[DateRange(start_date=start_date.isoformat(), end_date=end_date.isoformat())],
    )

    # Run the report
    response = client.run_report(request)

    # Process the results, filtering for paths starting with '/YYYY'
    page_views_data = {}
    year_pattern = re.compile(r'^/\d{4}')
    for row in response.rows:
        page_path = row.dimension_values[0].value
        if year_pattern.match(page_path):
            page_views = int(row.metric_values[0].value)
            page_views_data[page_path] = page_views

    # Write data to YAML file
    filename = f"page_views_year_based_{start_date.isoformat()}_{end_date.isoformat()}.yaml"
    with open(filename, 'w') as file:
        yaml.dump(page_views_data, file)

    print(f"Page views data for year-based paths over the last 6 months has been written to {filename}")

if __name__ == "__main__":
    # Replace with your actual GA4 property ID
    GA4_PROPERTY_ID = "YOUR_GA4_PROPERTY_ID"
    get_page_views(GA4_PROPERTY_ID)