function getBathValue(){
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1;
}
  
function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1;
}
  
function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_house_price"; 
  
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    },function(data, status) {
        console.log(data.predicted_price);
        estPrice.innerHTML = "<h2 style='color:#000'>" + data.predicted_price.toString() + " Lakh</h2> \n<h4 style='color:#FFF'>Accuracy Rate : 86.55 %</h4>";
        console.log(status);
    });
}
  
function onPageLoad() {
    console.log( "document loaded" );

    var url = "http://127.0.0.1:5000/get_location"; 

    $.get(url,function(data, status) {
        console.log("got response for get_location request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}
  
window.onload = onPageLoad;