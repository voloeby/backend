var size = null;
var color = null;

function chose_size(new_size){
	if(size==new_size){
		return;
	}
	else{
		var prev = $('#size_'+size).find('a');
		prev.css('border-style', 'none');
	}
	var tag = $('#size_'+new_size).find('a');
	tag.css('padding-left', '7px');
	tag.css('padding-right', '7px');
	tag.css('border-style', 'solid');
	tag.css('border-color', 'black');
	size = new_size;
}

function chose_color(new_color){
	if(color==new_color){
		return;
	}
	else{
		var prev = $('#color_'+color).find('a');
		prev.css('border-style', 'none');
	}
	var tag = $('#color_'+new_color).find('a');
	tag.css('padding-left', '7px');
	tag.css('padding-right', '7px');
	tag.css('border-style', 'solid');
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
	console.log('fff');
}
