CREATE database real_estate;
USE real_estate;

-- Create Properties table
CREATE TABLE Properties (
   property_id INT PRIMARY KEY AUTO_INCREMENT,
   property_name VARCHAR(255) NOT NULL,
   location VARCHAR(100) NOT NULL,
   area_sqft DECIMAL(12,2) NOT NULL CHECK (area_sqft > 0),
   year_constructed INT NOT NULL CHECK (year_constructed >= 1800),
   market_value DECIMAL(15,2) NOT NULL CHECK (market_value > 0)
);

-- Create MarketTrends table
CREATE TABLE MarketTrends (
   trend_id INT PRIMARY KEY AUTO_INCREMENT,
   year INT NOT NULL,
   location VARCHAR(100) NOT NULL,
   avg_price_per_sqft DECIMAL(12,2) NOT NULL CHECK (avg_price_per_sqft > 0)
);

SELECT COUNT(*) FROM Properties;
SELECT COUNT(*) FROM MarketTrends;
