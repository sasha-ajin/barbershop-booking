console.log('Js file works')

var form = document.getElementById('form')
csrftoken = form.getElementsByTagName("input")[0].value
//console.log('NewToken:',form.getElementsByTagName("input")[0].value)

form.addEventListener('submit', function (e) {
    e.preventDefault()
    if (confirm('Are you sure' + ' you want to book your time with ' + form.barber.value + ' for tomorrow in ' +
        form.time.value + '?')) {
        booking()
    }
})

function booking() {

    var bookInfo = {
        'barber': form.barber.value,
        'name': form.name.value,
        'phone': form.phone.value,
        'email': form.email.value,
        'time': form.time.value
    }
    console.log(bookInfo)

    var url = '/process_booking'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'form': bookInfo})


    })
        .then((response) => response.json())
        .then((data) => {
            console.log('Success', data)
            alert('You booked your time with ' + form.barber.value + ' for tomorrow in ' + form.time.value)
            window.location.href = "/"
        })
}
