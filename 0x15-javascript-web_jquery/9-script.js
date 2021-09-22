$.get('https://fourtonfish.com/hellosalut/?lang=fr', say => {
  $('DIV#hello').text(say.hello);
});
