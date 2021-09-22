$.get('https://fourtonfish.com/hellosalut/?lang=fr', say => {
  $('#hello').text(say.hello);
});
