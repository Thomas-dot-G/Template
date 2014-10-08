// Executes the 'onLoad' function after loading the page
document.addEventListener('DOMContentLoaded', onLoad);

function getPlayerData(fn) {
  $.ajax("/project/api/players")
    .done(fn)
    .fail(function(msg) {
      console.error('AJAX request failed:', msg);
    });
}

function onLoad() {
  // On change in the #filter-players input, compute the table again
  // by filtering rows
  $('#filter-players').on('input', filterPlayers);
}

// Create DOM elements from the data
function updatePlayers(rows) {
  var f = document.createDocumentFragment();
  rows.forEach(function(r) {
    var tr = document.createElement('tr');

    $('<td>')
      .text(r.name)
      .appendTo(tr);

    $('<td>')
      .text(r.age)
      .appendTo(tr);

    var link = $('<a>')
      .text('Matches ')
      .attr('href', '/project/player_details/' + r.name + '/');

    var span = $('<span>')
      .addClass('badge')
      .text(r.matchesCount)
      .appendTo(link);

    $('<td>')
      .append(link)
      .appendTo(tr);

    f.appendChild(tr);
  });

  $('table tbody')
    .empty()
    .append(f);
}

function filterPlayers(event) {
  var playerFilter = event.target.value;

  getPlayerData(function(rows) {
    // Filter rows when playerFilter is a non-empty string
    if (playerFilter.length > 0) {
      rows = rows.filter(function(r) {
        return r.name.toLowerCase().contains(playerFilter.toLowerCase());
      });
    }

    updatePlayers(rows);
  });
}

// Polyfill for String.contains
if ( !String.prototype.contains ) {
    String.prototype.contains = function() {
        return String.prototype.indexOf.apply( this, arguments ) !== -1;
    };
}
