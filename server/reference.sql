CREATE TABLE corporations(
    id serial PRIMARY KEY,
    name text UNIQUE NOT NULL,
    symbol text UNIQUE NOT NULL
);

CREATE TABLE stocks(
    id serial PRIMARY KEY,
    corporation_id integer REFERENCES corporations(id),
    closing_value decimal NOT NULL,
    highest_value decimal NOT NULL,
    day_prediction_value decimal NOT NULL,
    week_prediction_value decimal NOT NULL,
    month_prediction_value decimal NOT NULL,
    record_date date NOT NULL
);