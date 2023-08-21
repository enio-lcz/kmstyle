def get_latest_email(userId):
    """
    查询Gmail邮箱中最后一封邮件信息
    :param userId: 必要参数，字符串类型，用于表示需要查询的邮箱ID，\
    注意，当查询我的邮箱时，userId需要输入'me'；
    :return：包含最后一封邮件全部信息的对象，该对象由Gmail API创建得到，且保存为JSON格式
    """
    # 从本地文件中加载凭据
    creds = Credentials.from_authorized_user_file('token.json')
    
    # 创建 Gmail API 客户端
    service = build('gmail', 'v1', credentials=creds)
    
    # 列出用户的一封最新邮件
    results = service.users().messages().list(userId=userId, maxResults=1).execute()
    messages = results.get('messages', [])

    # 遍历邮件
    for message in messages:
        # 获取邮件的详细信息
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        
    return json.dumps(msg)
