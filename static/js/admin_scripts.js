var id = 0;

function del_item(id){
	var csrf = $('#csrf_token').html();
	var loc = $('#edit_link_'+id).attr('href');
	$.ajax({url:loc, method:'delete', headers:{ 'X-CSRFToken':csrf}, data:{csrfmiddlewaretoken:csrf}, success: function(res){
		$("#"+id).remove();
	}});
}

function upd_show(id){
	var loc = $('#edit_link_'+id).attr('href');
	var csrf = $('#csrf_token').html();
	$.ajax({url:loc, method:'patch', headers:{ 'X-CSRFToken':csrf}, data:{'csrfmiddlewaretoken':csrf}, success: function(res){
		// $("#"+id).remove();
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
		console.log($("#image_upload")[0].files[0]);
		fd.append('file', $("#image_upload")[0].files[0]); // console.log(inp.val());
		// 'csrfmiddlewaretoken':csrf
		console.log(csrf);
		fd.append('csrfmiddlewaretoken', csrf);
		$.ajax({
			url: '/admin/shop/item/' + id + '/item_image',
			headers:{ 'X-CSRFToken':csrf},
			method: 'post',
			data: fd,
			success: function (res) {
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
	})
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
