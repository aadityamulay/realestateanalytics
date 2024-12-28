import pytest
from realestateanalytics import RealEstateData, RealEstateAnalytics

# Test the data generation (pytest realestatetest.py)
def test_property_generation():
    generator = RealEstateData()
    properties = generator.generate_properties(num_properties=5)
    
    # Basic checks
    assert len(properties) == 5
    assert isinstance(properties[0]['property_name'], str)
    assert properties[0]['location'] in generator.LOCALITIES
    assert 500 <= properties[0]['area_sqft'] <= 2500
    assert 1990 <= properties[0]['year_constructed'] <= 2023

# Test the analytics
def test_analytics():
    # Create some test data
    test_properties = [
        {
            'property_name': 'Test Property 1',
            'location': 'CIDCO',
            'area_sqft': 1000,
            'year_constructed': 2020,
            'market_value': 10000
        },
        {
            'property_name': 'Test Property 2',
            'location': 'Garkheda',
            'area_sqft': 1500,
            'year_constructed': 2021,
            'market_value': 15000
        }
    ]
    
    test_trends = [
        {
            'year': 2022,
            'location': 'CIDCO',
            'avg_price_per_sqft': 5000
        }
    ]
    
    # Run analytics
    analytics = RealEstateAnalytics()
    results = analytics.perform_analytics(test_properties, test_trends)
    
    # Check if we got all expected results
    assert "property_summary" in results
    assert "avg_price_by_location" in results
    assert "yearly_avg_trends" in results