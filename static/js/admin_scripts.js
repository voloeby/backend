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
