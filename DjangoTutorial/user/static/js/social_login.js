function buildQuery(params) {
    return Object.keys(params).map(function (key) {return key + '=' + encodeURIComponent(params[key])}).join('&')
}
function buildUrl(baseUrl, queries) {
    return baseUrl + '?' + buildQuery(queries)
}

function naverLogin() {
    params = {
        response_type: 'code',
        client_id:'WtaECQMXs_Y5B3CVhI0b',
        redirect_uri: location.origin + '/user/login/social/naver/callback/' + location.search,
        state: document.querySelector('[name=csrfmiddlewaretoken]').value
    }
    url = buildUrl('https://nid.naver.com/oauth2.0/authorize', params)
    location.replace(url)
}