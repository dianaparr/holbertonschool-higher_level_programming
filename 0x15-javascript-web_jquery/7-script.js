$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', personName => {
  $('DIV#character').text(personName.name);
});
