def get_email_count(userId):
    """
    查询Gmail邮箱中的邮件数量
    :param userId: 必要参数，字符串类型，用于表示需要查询的邮箱ID，\
    注意，当查询我的邮箱时，userId需要输入'me'；
    :return：包含邮件数量的对象，该对象由Gmail API返回，并以JSON格式保存。
    """
    # 从本地文件中加载凭据
    creds = Credentials.from_authorized_user_file('token.json')
    
    # 创建 Gmail API 客户端
    service = build('gmail', 'v1', credentials=creds)
    
    # 获取邮箱中的邮件数量
    results = service.users().messages().list(userId=userId, maxResults=1).execute()
    total_count = results['resultSizeEstimate']
    
    # 将结果保存为JSON格式对象
    result_object = {'email_count': total_count}
    
    return json.dumps(result_object)