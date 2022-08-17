document.body.addEventListener('click',
    function (e) {
        var timecode = null
        var parts, seconds, minutes, hours
        var iframe = document.body.querySelector('iframe[src^="https://share.transistor.fm/e/"]')
        var url, hashPos

        if (!iframe) {
            console.warn('No Transistor episode player found.')
            return
        }

        if (e.target.classList.contains('transcript-timecode')) {
            timecode = e.target
        } else {
            timecode = e.target.closest('.transcript-timecode')
        }

        if (!timecode) {
            return
        }

        e.preventDefault()
        timecode = timecode.innerText
        parts = timecode.split(':')

        if (!parts.length) {
            console.warn('Invalid timecode format')
            return
        }

        seconds = parseInt(parts.pop())

        if (parts.length) {
            minutes = parseInt(parts.pop())

            if (parts.length) {
                hours = parseInt(parts.pop())

                if (parts.length) {
                    console.warn('Invalid timecode format')
                    return
                }
            }
        }

        minutes += (hours * 60)
        url = iframe.getAttribute('src')
        hashPos = url.indexOf('#')

        if (hashPos !== -1) {
            url = url.substr(0, hashPos)
        }

        url += '#t=' + minutes + 'm' + seconds + 's'
        iframe.setAttribute('src', url)
    }
)
