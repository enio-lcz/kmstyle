def get_email_info(userId='me', n=1):
    """
    获取指定邮箱的第一封邮件的信息。

    参数：
    userId: 要查询的邮箱的用户ID，默认为'me'，表示当前授权的用户。
    n: 要查询的邮件的索引，默认为1，表示查询第一封邮件。

    返回：
    一个字典，包含邮件的收件时间、发送人和邮件内容的键值对，键包括 '收件时间'、'发送人' 和 '邮件内容'。
    """
    # 从本地文件中加载凭据
    creds = Credentials.from_authorized_user_file('token.json')

    # 创建 Gmail API 客户端
    service = build('gmail', 'v1', credentials=creds)

    # 查询邮件列表
    results = service.users().messages().list(userId=userId).execute()
    messages = results.get('messages', [])[:n]

    email_info = {}

    if messages:
        message = messages[0]
        msg = service.users().messages().get(userId=userId, id=message['id']).execute()

        # 解码邮件内容
        payload = msg['payload']
        headers = payload.get("headers")
        parts = payload.get("parts")

        if headers:
            for header in headers:
                name = header.get("name")
                if name.lower() == "from":
                    email_info['发送人'] = header.get("value")
                if name.lower() == "date":
                    email_info['收件时间'] = parser.parse(header.get("value")).strftime('%Y-%m-%d %H:%M:%S')

        if parts:
            for part in parts:
                mimeType = part.get("mimeType")
                body = part.get("body")
                if mimeType == "text/plain":
                    data_decoded = base64.urlsafe_b64decode(body.get("data")).decode()
                    email_info['邮件内容'] = data_decoded
                elif mimeType == "text/html":
                    data_decoded = base64.urlsafe_b64decode(body.get("data")).decode()
                    soup = BeautifulSoup(data_decoded, "html.parser")
                    email_info['邮件内容'] = soup.get_text()

    return json.dumps(email_info)