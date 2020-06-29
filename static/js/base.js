const indicator = document.querySelector('.nav-indicator');
const items = document.querySelectorAll('.nav-item');

function handleIndicator(el) {
  items.forEach(item => {
    item.classList.remove('is-active');
    item.removeAttribute('style');
  });
  
  indicator.style.width = `${el.offsetWidth}px`;
  indicator.style.left = `${el.offsetLeft}px`;
  indicator.style.backgroundColor = el.getAttribute('active-color');

  el.classList.add('is-active');
  el.style.color = el.getAttribute('active-color');
}


items.forEach((item, index) => {
  item.addEventListener('click', (e) => { handleIndicator(e.target)});
  item.classList.contains('is-active') && handleIndicator(item);
});

var $cards = $('.card-object'),
    $faceButtons = $('.face');

$faceButtons.on('click', flipCard);

function flipCard(event) {
  event.preventDefault();
  
  var $btnFace = $(this),
      $card = $btnFace.parent('.card-object');
  
  if( $card.hasClass('flip-in') ) {
    closeCards();
  } else {
    closeCards();
    openCard($card);
  }
  
}

function closeCards() {
  $cards.each( function() {
    $(this)
      .filter('.flip-in')
      .removeClass('flip-in')
      .queue( function() {
        // Force reflow hack
        var reflow = this.offsetHeight;
        $(this)
          .addClass('flip-out')
          .dequeue();
      })
      
  });
}

function openCard($card) {
  $card
    .removeClass('flip-out')
    .queue( function() {
      // Force reflow hack
      var reflow = this.offsetHeight;
      $(this)
        .addClass('flip-in')
        .dequeue();
    });
    
}

function showModal(image_id,name,description,url,location,category,category_id,posted){
  $("#img-name").text(name)
  $("#imageModal").modal("show")
  $(".modal-title").text(name)
  $(".mod-img").attr("src",url)
  $("#img-desc").text(description)
  $("#img-loc").text(location)
  var link = "/category/" + category_id
  $("#img-cat").attr("href", link)
  $("#img-cat").text("#" + category)
  $("#img-pos").text(posted)
  $("#copy-url").val(window.location.origin + "/image/" + image_id)
}

function share(){
  $("#copy-url").select()
  document.execCommand('copy');
  alert("Share link has been copied to your clipboard!")
}

