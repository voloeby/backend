var size = null;
var color = null;

function chose_size(new_size){
	if(size==new_size){
		return;
	}
	else{
		var prev = $('#size_'+size).find('a');
		prev.css('border-color', 'transparent');
	}
	var tag = $('#size_'+new_size).find('a');
	tag.css('border-color', 'black');
	size = new_size;
}

function chose_color(new_color){
	if(color==new_color){
		return;
	}
	else{
		var prev = $('#color_'+color).find('a');
		prev.css('border-color', 'transparent');
	}
	var tag = $('#color_'+new_color).find('a');
	tag.css('border-color', 'black');
	color = new_color;
}

function new_pre_order(){
	console.log($(location).attr('pathname').split('/').slice(0,-2).join('/'));
	$('#email_input').css('border-color', '#252525')
	$('#city_input').css('border-color', '#252525')
	$('#error_box').css('display', 'none');
	$('#success_box').css('display', 'none');
	if(size==null && color==null){
		$('#error_message').text('Выберите размер и цвет.');
		$('#error_box').css('display', 'block');
		return;
	}
	if(size==null){
		$('#error_message').text('Выберите размер.');
		$('#error_box').css('display', 'block');
		return;
	}
	if(color==null){
		$('#error_message').text('Выберите цвет.');
		$('#error_box').css('display', 'block');
		return;
	}
	var email = $('#email_input').val();
	var city = $('#city_input').val();
	var csrf = $('#csrf_token').text();
	if (email=='') {
		$('#email_input').css('border-color', 'red')
		$('#error_message').text('Заполните поле email.');
		$('#error_box').css('display', 'block');
		return;
	}
	if(city==''){
		$('#city_input').css('border-color', 'red')
		$('#error_message').text('Заполните поле "Куда доставить".');
		$('#error_box').css('display', 'block');
		return;
	}

	$.ajax({url:$(location).attr('href'), method:'post', headers:{ 'X-CSRFToken':csrf}, data:{'email':email, 'city': city, 'size':size, 'color': color}, success: function(res){
		$('#success_message').text('Предзаказ успешно оформлен.');
		$('#success_box').css('display', 'block');
		$('#button').attr('href', $(location).attr('pathname').split('/').slice(0,-2).join('/'))
		$('#button').text('Перейти к магазину.')
	}});

}

function subscribe_to_news(){
	var csrf = $('#csrf_token').text();
	var email = $('#mc-email').val();
	if(email=='') return;
	console.log(email);
	$.ajax({url:'subscribe_to_email', method:'post', headers:{ 'X-CSRFToken':csrf}, data:{'email':email}, success: function(res){

		$('.subscribe-form').html('Вы успешно подписались на новости.');
	}});
}

var span = $('#about_surp');
var ch = "a";
function change_ch(){
	if(ch=="а"){
		ch = "е";
		span.text(ch);
	}
	else{
		ch = "а";
		span.text(ch);
	}
}
// span.click(()=>span.text('е'),()=>span.text('а'));

function to_main_image(image_id){
	var img = $('#image_'+image_id);
	var main_img = $('#main_image');
	var main_image_url = main_img.attr('src');
	console.log(main_image_url);
	main_img.attr('src', img.attr('src'));
	img.attr('src', main_image_url);
}
