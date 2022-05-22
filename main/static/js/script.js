let trackbar = $(".trackbar");
let current_audio = null;

document.getElementsByTagName("body")[0].onscroll = function myFunction() {
    let scrolltotop = document.scrollingElement.scrollTop;
    let target = document.getElementsByClassName("welcome")[0];
    let xvalue = "center";
    let factor = 0.7;
    let yvalue = scrolltotop * factor;
    target.style.backgroundPosition = xvalue + " " + yvalue + "px";
  }

$('.burger').on('click', function() {
    $('.header-values').toggleClass('active');
})

function play_track(track_container) {
    current_audio = track_container.children("audio")[0];
    current_audio.load();
    current_audio.currentTime = 0;
    current_audio.play();

    let track_name = "<b>" + track_container.find(".track-name").text() + "</b> — " + track_container.find(".track-user").text()
    trackbar.find(".trackbar-info").html(track_name);
    if (trackbar.css('display') === 'none')  {
        trackbar.css('display', "flex");
    }
}
$(document).on('click', '.track-info', function(e) {
  $(this).children().children('.circle').addClass('active');
  let pk = $(this).parent().children('audio').children().attr('id');
    $.ajax ({
      url: audio_listen_url,
      type: 'post',
      data: {
        audio_id: pk,
      },
      dataType: 'json'
    });
    let track_container = $(this).parent();
    if (current_audio !== null) {
        current_audio.pause()
    }
    play_track(track_container)
    $('.btn.play').attr("src", "/static/img/pause.svg");
    $('.btn.play').attr("class", "btn stop");
});


$(document).on('click', '.btn.play', function(e) {
    current_audio.play();
    $(this).children('.track-circle').children('.circle').addClass('active')
    $('.btn.play').attr("src", "/static/img/pause.svg");
    $('.btn.play').attr("class", "btn stop");
});


$(document).on('click', '.btn.stop', function(e) {
    current_audio.pause();
    $('.circle').removeClass('active');
    $('.btn.stop').attr("src", "/static/img/play.svg")
    $('.btn.stop').attr("class", "btn play")
});


$(document).on('click', '.prev, .next', function(e) {
    let audio_list = $('audio');

    let index;
    if ($(this).attr('class') == "btn prev") {
        index = audio_list.index(current_audio) - 1;
    } else {
        index = audio_list.index(current_audio) + 1;
    }

    if (index >= 0 && index < audio_list.length) {
        current_audio.pause()
        current_audio = audio_list[index];
    } else {
        return
    }
    let track_container = $(current_audio).parent();
    play_track(track_container)
    $('.btn.play').attr("src", "/static/img/pause.svg");
    $('.btn.play').attr("class", "btn stop");
});

$(document).on('mousemove mouseover', '.progress-container', function(e) {
    let posX = e.pageX - $(this).offset().left;
    let progressPercent = (posX / $(this).width()) * 100;
    progressPercent = parseFloat(progressPercent.toFixed(1));
    $('.progress-select').css('width', progressPercent.toString() + "%");
});


$(document).on('mouseout', '.progress-container', function(e) {
    $('.progress-select').css('width', "0%");
});


$(document).on('click', '.progress-container', function(e) {
    let posX = e.pageX - $(this).offset().left;
    let progressPercent = (posX / $(this).width()) * 100;
    progressPercent = parseFloat(progressPercent.toFixed(1));
    $('.progress').css('width', progressPercent.toString() + "%");
    let currentTime = progressPercent * (current_audio.duration/100);
    let is_paused = current_audio.paused;
    current_audio.load();
    current_audio.currentTime = currentTime;
    if (!is_paused) {
        current_audio.play();
    }
});


$('audio').on('timeupdate', function(e) { //ищем все элементы audio и присваиваем event timeupdate
    let progressPercent = (this.currentTime / this.duration) * 100; // вычисляем продолжительность
    $('.progress-container .progress').css('width', progressPercent.toString() + "%");
});
