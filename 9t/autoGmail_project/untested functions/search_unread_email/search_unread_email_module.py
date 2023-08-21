def search_unread_email(keyword, status):
    """
    查询未读的Gmail邮箱中包含关键词的邮件
    :param keyword: 必要参数，字符串类型，用于表示需要查询的关键词；
    :param status: 必要参数，字符串类型，用于表示需要查询的邮件状态，\
    可选择值为'unread'表示未读邮件，'read'表示已读邮件；
    :return: 包含未读邮件内容的对象，该对象由Gmail API创建得到，且保存为JSON格式
    """
    
    # 从本地文件中加载凭据
    creds = Credentials.from_authorized_user_file('token.json')

    # 创建 Gmail API 客户端
    service = build('gmail', 'v1', credentials=creds)
    
    # 组合查询语句
    query = f'is:{status} {keyword}'

    # 查询满足条件的未读邮件
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    # 存储所有符合条件的邮件内容
    email_contents = []

    # 遍历邮件
    for message in messages:
        # 获取邮件的详细信息
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        email_contents.append(msg['snippet'])

    return json.dumps(email_contents)