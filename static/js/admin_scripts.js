var id = 0;

function del_item(id){
	var csrf = $('#csrf_token').html();
	var loc = $('#edit_link_'+id).attr('href');
	$.ajax({url:loc, method:'delete', headers:{ 'X-CSRFToken':csrf}, data:{csrfmiddlewaretoken:csrf}, success: function(res){
		$("#"+id).remove();
	}});
}

function upd_show(id){
	var loc = $('#edit_link_'+id).attr('href') + '?type=show';
	var csrf = $('#csrf_token').html();
	$.ajax({url:loc, method:'patch', headers:{ 'X-CSRFToken':csrf}, data:{'type':'show'}, success: function(res){
	}});
}

function upd_user(user_id){
	var loc = '/admin/users/update'
	var csrf = $('#csrf_token').html();
	$.ajax({url:loc, method:'post', headers:{ 'X-CSRFToken':csrf}, data:{'user_id':user_id, 'type': 'is_active'}, success: function(res){

	}});
}

function del_post(id){
	var csrf = $('#csrf_token').html();
	var loc = $('#edit_link_'+id).attr('href');
	$.ajax({url:loc, method:'delete', headers:{ 'X-CSRFToken':csrf}, data:{csrfmiddlewaretoken:csrf}, success: function(res){
		$("#"+id).remove();
	}});
}

function new_item_image(id){
	$('#image_upload').trigger('click');
}

$(()=>{
	id = $('h1').attr('id');
	$('#image_upload').change(()=>{
		//send file to server
		var csrf = $('#csrf_token').html();
		var inp = $('#image_upload');
		if (inp.val() == '') {
			return;
		}
		var fd = new FormData();
		// console.log($("#image_upload")[0].files[0]);
		fd.append('file', $("#image_upload")[0].files[0]); // console.log(inp.val());
		// 'csrfmiddlewaretoken':csrf
		// console.log(csrf);
		fd.append('csrfmiddlewaretoken', csrf);
		$.ajax({
			url: '/admin/shop/item/' + id + '/item_image',
			headers:{ 'X-CSRFToken':csrf},
			method: 'post',
			data: fd,
			success: function (res) {
				console.log(res);
				var image_url = JSON.parse(res).image;
				var image_id = JSON.parse(res).id;
				var div = $('#none-image').clone().attr('id', image_id);
				div.css('display', 'block');
				console.log(div);
				div.find('img').attr('src', image_url);
				div.find('a').attr('href', 'javascript:del_image('+image_id+')');
				console.log(div);
				$('#images').append(div);
				$('#images').append($('#add_but'));
			},
			processData: false,
			contentType: false
		});
	});
	$.fn.moveUp = (tag_id)=>{;
		before = $('#'+tag_id).prev();
		$('#'+tag_id).insertBefore(before);
	}

	$.fn.moveDown = (tag_id)=>{
		after = $('#'+tag_id).next();
		$('#'+tag_id).insertAfter(after);
	}
});


function del_image(image_id){
	var csrf = $('#csrf_token').html();
	$.ajax({
		url: '/admin/shop/item/'+id+'/item_image',
		headers:{ 'X-CSRFToken':csrf},
		method: 'delete',
		data: {image_id: image_id, csrfmiddlewaretoken: csrf},
		success: function(res){
			$('#'+image_id).remove()
		}
	})
}

var is_income = null;

function add_finance(str){
	if(str == '+') is_income = true;
	else is_income = false;
	console.log($('#pop_up_window'));
	$('#pop_up_window').css('display', 'block');
	console.log($('#pop_up_window').css('display'));
}

function send_finance(){
	var csrf = $('#csrf_token').html();
	var data = $('#new_finance_form').serializeArray().reduce((obj, item)=>{
		obj[item.name] = item.value;
    	return obj;
	},{});
	data.is_income = is_income;
	$.ajax({
		url: '/admin/finances',
		headers:{ 'X-CSRFToken':csrf},
		method: 'post',
		data: data,
		success: (res)=>{
			if (res == 'ok') {
				$('#pop_up_window').css('display', 'none');
				document.location.href = '/admin/finances';
			}
		}
	});
}

function del_finance(fin_id){
	var csrf = $('#csrf_token').html();
	$.ajax({
		url: '/admin/finances',
		headers:{ 'X-CSRFToken':csrf},
		method: 'delete',
		data: {'id': fin_id},
		success: (res)=>{
			console.log(res);
			if (res == 'ok') {
				$('#'+fin_id).remove();
			}
		}
	});
}



function close_win(tag_id){
	$('#'+tag_id).css('display', 'none');
}

function move_up_product(product_id){
	var csrf = $('#csrf_token').html();
	$.ajax({
		url: '/admin/shop/item/edit/'+product_id+'?type=move_up',
		headers:{ 'X-CSRFToken':csrf},
		method: 'patch',
		data: {},
		success: (res)=>{
			if (res != 'no_change'){
				$('#'+product_id).moveUp(product_id)
			}
		}
	});
}

function move_down_product(product_id){
	var csrf = $('#csrf_token').html();
	$.ajax({
		url: '/admin/shop/item/edit/'+product_id+'?type=move_down',
		headers:{ 'X-CSRFToken':csrf},
		method: 'patch',
		data: {},
		success: (res)=>{
			if (res != 'no_change'){
				$('#'+product_id).moveDown(product_id);
			}
		}
	});
}


function really_delete(func, arg=null){
	$('#pop_up_window_delete').css('display', 'block');
	$('.dark-back').focus();
	$('#delete_button').click(()=>{
		func(arg);
		$('#pop_up_window_delete').css('display', 'none');
	});
}
