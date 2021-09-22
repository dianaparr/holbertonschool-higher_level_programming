document.addEventListener('DOMContentLoaded', () => {
  $('INPUT#btn_translate').click(() => {
    const languages = $('INPUT#language_code').val();
    $.getJSON('https://www.fourtonfish.com/hellosalut/' + '?lang=' + languages, sayHello => {
      $('DIV#hello').text(sayHello.hello);
    });
  });
});
