//Initialize google maps
function initMap() {
        var uluru = {lat: -25.363, lng: 131.044};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: uluru
        });
        var geocoder = new google.maps.Geocoder();
        document.getElementById('submit').addEventListener('click', function() {
          geocodeAddress(geocoder, map);
        });
      }

//Search location by address in google maps
function geocodeAddress(geocoder, resultsMap) {
  var address = document.getElementById('address').value;
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === 'OK') {
      resultsMap.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
        map: resultsMap,
        position: results[0].geometry.location
      });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}


function registerBusiness(){
     var section = document.getElementById('mainSection');
     if(section != undefined)
     {
        section.remove();
     }
     $("#registerpnl").show('slow');

}


//Upload picture
/*$('document').on('change', ':file', function() {

        var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
        input.trigger('fileselect', [numFiles, label]);
        $('#filetext').attr('value',label);
});*/


$('document').ready(function(){


    $(':file').on('fileselect', function(event, numFiles, label) {

        console.log(numFiles);
        console.log(label);
    });

    $('#selectimg').on('click', function(){

          var img=$('input:file').val();
          console.log(img);
          $("#avatar").attr('src',img);

    });

    // Hide play button on start
    $("#playmusic").hide(100);

    //Stop website music
    $("#stopmusic").click(function(){

      $("#stopmusic").hide(100);
      var music = document.getElementById("music");
      music.muted = true;
      $("#playmusic").show(100);
    })

    //Start website music
    $("#playmusic").click(function(){

      $("#playmusic").hide(100);
      var music = document.getElementById("music");
      music.muted = false;
      $("#stopmusic").show(100);
    })

    $("#login").click(function(){

       var section = document.getElementById('mainSection');
       if(section != undefined)
       {
         section.remove();
       }
       $("#searchpnl").hide();
       $("#registerpnl").hide();
       $("#signuppnl").hide();
       $("#loginpnl").slideToggle('slow');

      })

    $("#search").click(function(){


      var section = document.getElementById('mainSection');
      if(section != undefined)
      {
        section.remove();
      }
       $("#loginpnl").hide();
       $("#registerpnl").hide();
       $("#signuppnl").hide();
       $("#searchpnl").slideToggle('slow');

    })

    $("#register").click(function(){

      var section = document.getElementById('mainSection');
      if(section != undefined)
      {
        section.remove();
      }
       $("#loginpnl").hide();
       $("#searchpnl").hide();
       $("#signuppnl").hide();
       $("#registerpnl").slideToggle('slow');

    })

    $("#signup").click(function(){

      var section = document.getElementById('mainSection');
      if(section != undefined)
      {
        section.remove();
      }
      $("#loginpnl").hide();
      $("#searchpnl").hide();
      $("#registerpnl").hide();
      $("#signuppnl").slideToggle('slow');

    })

    $('.flip').hover(function(){
        $(this).find('.card').toggleClass('flipped');
    });

    $('.play').click(function(){
      $('.video-player').css('display','block');
    });

    function createCookie(name, value, days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        var expires = "; expires=" + date.toGMTString();
    } else var expires = "";
    document.cookie = name + "=" + value + expires + "; path=/";
    }

    function readCookie(name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }

    function eraseCookie(name) {
        createCookie(name, "", -1);
    }

    var $body = $("body"),
        sCookieName = "cookiewarning",
        $cookiewarning = $("div." + sCookieName);

    function setCookieWarning(active) {
        (!!active) ? $body.addClass(sCookieName): $body.removeClass(sCookieName)
    }

    $cookiewarning.on("click", function() {
        createCookie(sCookieName, 1, 365)
        setCookieWarning(false);
    });

    // cookie warning
    if (readCookie(sCookieName) != 1) {
        setCookieWarning(true);
    }

    $(".removecookie").on("click", function() {
        eraseCookie(sCookieName);
        setCookieWarning(false);
    })

    var $videoSrc;
$('.video-btn').click(function() {
    $videoSrc = $(this).data( "src" );
});
console.log($videoSrc);



// when the modal is opened autoplay it
$('#myModal').on('shown.bs.modal', function (e) {

// set the video src to  autoplay and not to show related video.
//$("#video").attr('src',$videoSrc + "?rel=0&amp;showinfo=0&amp;modestbranding=1&amp;autoplay=0" );
$("#video").attr('src',$videoSrc + "?rel=0&amp;showinfo=0&amp;modestbranding=1&amp" );

})


// stop playing the youtube video when I close the modal
$('#myModal').on('hide.bs.modal', function (e) {
    // a poor man's stop video
    $("#video").attr('src',$videoSrc);
})


})




//Validate credit card number/iban

//Validate expiration date








