def get_email_communication(userId):
    """
    查询我与指定用户之间的邮件通信记录
    :param userId: 必要参数，字符串类型，表示与谁的邮件通信记录，可以是邮箱地址或用户名等。
    :return: 包含邮件通信记录的对象，该对象由Gmail API返回，且保存为JSON格式。
    """
    # 从本地文件中加载凭据
    creds = Credentials.from_authorized_user_file('token.json')
    
    # 创建 Gmail API 客户端
    service = build('gmail', 'v1', credentials=creds)
    
    # 获取用户的邮件通信记录
    results = service.users().messages().list(userId='me', q=f"from:{userId} OR to:{userId}").execute()
    messages = results.get('messages', [])
    
    # 遍历邮件并获取详细信息
    communication_records = []
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        communication_records.append(msg)
    
    return json.dumps(communication_records)