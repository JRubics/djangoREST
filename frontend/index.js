function showHotels(event) {
    $.ajax({
        url : "http://localhost:8000/hotels/",
        type:"GET",
		contentType: "application/json; charset=utf-8",
        dataType: "json",
        success : function (data) {
            alert(JSON.stringify(data))
        },
        error: function (message) {
            alert(message.status)
        },
    });
}