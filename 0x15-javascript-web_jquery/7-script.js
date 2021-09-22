$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', personName => {
  $('#character').text(personName.name);
});
