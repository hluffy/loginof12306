import requests
import test
import user

req = requests.Session()

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/63.0.3239.84 Safari/537.36'
}
def singin():
    #获取验证码
    response = req.get('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&'
            '0.02982654119162098')
    # print(response.text)
    codeImg = response.content
    fn = open('code.png','wb')
    fn.write(codeImg)
    fn.close()
    print('验证码保存成功')

    codestr = input('请输入验证码序号: ')
    codelist = codestr.split(',')
    codes = []
    for i in codelist:
        code = test.getcode(int(i))
        codes.append(code)
        pass
    print(codes)

    code = ''
    for i in codes:
        code = code + ',' + i
        pass

    # print(code[1:])
    #验证码校验
    data = {
        'answer': code[1:],
        'login_site':'E',
        'rand': 'sjrand'
    }
    response = req.post('https://kyfw.12306.cn/passport/captcha/captcha-check',data = data,
             headers = headers)

    print(response.text)
    result = response.json()
    if result['result_code'] == '4':
        print('验证码校验成功')
    else:
        print('验证码校验失败')
        singin()
        return

    data = {
        'username': user.username,
        'password': user.password,
        'appid': 'otn'
    }
    response = req.post('https://kyfw.12306.cn/passport/web/login',data = data,headers = headers)
    result = response.json()
    print(response.text)

    if result['result_code'] == 0:
        # url = 'https://kyfw.12306.cn/otn/leftTicket/query'
        url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-01-16&leftTicketDTO.f' \
              'rom_station=SHH&leftTicketDTO.to_station=XAY&purpose_codes=ADULT'
        data = {
            'leftTicketDTO.train_date': '2018 - 01 - 16',
            'leftTicketDTO.from_station': 'SHH',
            'leftTicketDTO.to_station': 'XAY',
            'purpose_codes': 'ADULT'
        }
        response = req.get(url)
        print(response.content)
        pass
    else:
        print('登录失败')


singin()