$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr('data-url'),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-element').modal('show');
			},
			success: function(data){
				$('#modal-element .modal-content').html(data.html_form);
			}
		});
	};



	var SaveForm =  function(){
		var form = $(this);

		$.ajax({
			url: form.attr("data-url"),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#element-table tbody').html(data.element_list);
					$('#modal-element').modal('hide');

				} else {
					$('#modal-element .modal-content').html(data.html_form)
				}
			}

		})
		$('#element-table').DataTable().ajax.reload();
		return false;




	}

// create
$(".show-form").click(ShowForm);
$("#modal-element").on("submit",".create-form",SaveForm);

//update
$('#element-table').on("click",".show-form-update",ShowForm);
$('#modal-element').on("submit",".update-form",SaveForm)

//delete
$('#element-table').on("click",".show-form-delete",ShowForm);
$('#modal-element').on("submit",".delete-form",SaveForm)


});


$(document).ready(function(){
	var ShowForm_group = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr('data-url'),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-group').modal('show');
			},
			success: function(data){
				$('#modal-group .modal-content').html(data.html_form);
			}
		});


	};

	var SaveForm_group =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr("data-url"),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){

					$('#group-table tbody').html(data.group_list);
					$('#modal-group').modal('hide');
				} else {
					$('#modal-group .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

// create-group
$(".show-form2").click(ShowForm_group);
$("#modal-group").on("submit",".create-form",SaveForm_group);

//update-group
$('#group-table').on("click",".show-form-update",ShowForm_group);
$('#modal-group').on("submit",".update-form",SaveForm_group)

//delete-group
$('#group-table').on("click",".show-form-delete",ShowForm_group);
$('#modal-group').on("submit",".delete-form",SaveForm_group)
});