# FRS
FRS (Flight Reservation System) is Restfull API project with django rest framework.
1. Install modules in ```requirments.txt```
2. Make a copy from ```development.py.dist``` and rename it without ```.dist``` postfix.
 And fill you DB info on that. This projects use ```mariaDB``` as database.
3. ```/api/v1/users/``` create new user 
4. ```/api/v1/login/``` login API.
This api will return a JWT token.
4. use that token to
 get ```/api/v1/flights/?search=```,
 create ```api/v1/flights/```, 
update ```/api/v1/flights/{pk}/```
an delete ```/api/v1/flights/{pk}``` flights.
Feel free to ask aby question.
