def retrieve_emails(n, user_id='me'):
    """
    获取指定数量的最近邮件。

    参数:
    n: 要检索的邮件的数量。这应该是一个整数。
    user_id: 要检索邮件的用户的ID。默认值是'me'，表示当前授权的用户。

    返回:
    一个列表，其中每个元素都是一个字典，表示一封邮件。每个字典包含以下键：
    'From': 发件人的邮箱地址。
    'Date': 邮件的发送日期。
    'Subject': 邮件的主题。
    'Snippet': 邮件的摘要（前100个字符）。
    """
    # 从本地文件中加载凭据
    creds = Credentials.from_authorized_user_file('token.json')

    # 创建 Gmail API 客户端
    service = build('gmail', 'v1', credentials=creds)

    # 获取邮件列表
    results = service.users().messages().list(userId=user_id).execute()
    messages = results.get('messages', [])[:n]

    emails = []
    for message in messages:
        msg = service.users().messages().get(userId=user_id, id=message['id']).execute()

        # 解码邮件内容
        payload = msg['payload']
        headers = payload.get("headers")
        parts = payload.get("parts")

        data = {}

        if headers:
            for d in headers:
                name = d.get("name")
                if name.lower() == "from":
                    data['From'] = d.get("value")
                if name.lower() == "date":
                    data['Date'] = parser.parse(d.get("value")).strftime('%Y-%m-%d %H:%M:%S')
                if name.lower() == "subject":
                    data['Subject'] = d.get("value")

        if parts:
            for part in parts:
                mimeType = part.get("mimeType")
                body = part.get("body")
                data_decoded = base64.urlsafe_b64decode(body.get("data")).decode()
                if mimeType == "text/plain":
                    data['Snippet'] = data_decoded
                elif mimeType == "text/html":
                    soup = BeautifulSoup(data_decoded, "html.parser")
                    data['Snippet'] = soup.get_text()

        emails.append(data)

    # 返回邮件列表
    return json.dumps(emails, indent=2)
