/*message='Are you sure you want to delete?';
result = window.confirm(message);
*/

$( document ).ready(function(){
    function initialize() {
        /* after you calculate the locations, plug into this js fxn*/
        // Use jinja to pull longlat var
      var myLatlng = new google.maps.LatLng(-25.363882,131.044922);
      var mapOptions = {
        zoom: 4,
        center: myLatlng
      }
      var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

      var marker = new google.maps.Marker({
          position: myLatlng,
          map: map,
          title: 'Hello World!'
      });

    }
    var result=google.maps.event.addDomListener(window, 'load', initialize);

    $('#bttn').onclick(result)
)

