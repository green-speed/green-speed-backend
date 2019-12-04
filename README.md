# green-speed-backend

The application is created as a project for Bolzano hackathon (NOI Technopark).

The main idea is to develop app, which would show the route from point A to point B with a green-score level, which means how much is this transport good for the environment. 

The app uses API from SASA buses, car-sharing, bike-sharing in South Tyrol. 

# flask_app

Example of usage: 

http://127.0.0.1:5000/route?from_x=45&from_y=45&to_x=76&to_y=67

where:
from_x, from_y - latitude and longitude position from
to_x, to_y - latitude and longitude position to
