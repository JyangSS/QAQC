$(document).ready(function(){
	var ShowForm2 = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-type').modal('show');
			},
			success: function(data){
				$('#modal-type .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm2 =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#type-table tbody').html(data.type_list);
					$('#modal-type').modal('hide');

				} else {
					$('#modal-type .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

// create
$("#form2").click(ShowForm2);
$("#modal-type").on("submit","#form",SaveForm2);

//update
$('#type-table').on("click",".show-form-update",ShowForm2);
$('#modal-type').on("submit",".update-form",SaveForm2)

//delete
$('#type-table').on("click",".show-form-delete",ShowForm2);
$('#modal-type').on("submit",".delete-form",SaveForm2)
} );