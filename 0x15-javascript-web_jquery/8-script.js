$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', filmsData => {
  filmsData.results.forEach(filterMovie => {
    $('#list_movies').append('<li> ' + filterMovie.title + ' </li>');
  });
});
