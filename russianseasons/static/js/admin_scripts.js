function del_item(id){
	var csrf = $('#csrf_token').html();
	$.ajax({url:'shop/item/edit/'+id, method:'delete', headers:{ 'X-CSRFToken':csrf}, data:{csrfmiddlewaretoken:csrf}, success: function(res){
		console.log(res);
		$("#"+id).remove();
	}});
}

function upd_show(id){
	var csrf = $('#csrf_token').html();
	$.ajax({url:'shop/item/edit/'+id, method:'patch', headers:{ 'X-CSRFToken':csrf}, data:{csrfmiddlewaretoken:csrf}, success: function(res){
		// $("#"+id).remove();
	}});
}
