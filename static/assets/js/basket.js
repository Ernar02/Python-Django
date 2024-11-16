function basket_edit(event) {
    let t_href = event.target;
    $.ajax({
        url: '/basket/edit/' + t_href.name + '/' + t_href.value + '/',
        success: function (data) {
            $('.basket_list').html(data.result)
            $('.basket span').text(t_href.value)
        },
    });
    event.preventDefault();
}

window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function(event) {
        basket_edit(event)
    }).on('change', 'input[type="number"]', function(event) {
        basket_edit(event)
    });
}