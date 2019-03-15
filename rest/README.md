METHODS:
    HotelList:
        GET:
            curl http://localhost:8000/hotels/
        POST:
            curl -d 'title=mkyong&star_num=2' http://localhost:8000/hotels/
    HotelDetail:
        GET:
            curl http://localhost:8000/hotels/7/
        PUT(EDIT):
            curl -X PUT -d 'title=mkyong&star_num=2' http://localhost:8000/hotels/2/
        DELETE:
            curl -X DELETE http://localhost:8000/hotels/