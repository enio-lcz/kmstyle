def send_email(to, subject, message_text):
    """
    借助Gmail API创建并发送邮件函数
    :param to: 必要参数，字符串类型，用于表示邮件发送的目标邮箱地址；
    :param subject: 必要参数，字符串类型，表示邮件主题；
    :param message_text: 必要参数，字符串类型，表示邮件全部正文；
    :return：返回发送结果字典，若成功发送，则返回包含邮件ID和发送状态的字典。
    """
    
    creds_file='token_send.json'
    
    def create_message(to, subject, message_text):
        """创建一个MIME邮件"""
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = 'me'
        message['subject'] = subject
        raw_message = base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode('utf-8')
        return {
            'raw': raw_message
        }

    def send_message(service, user_id, message):
        """发送邮件"""
        try:
            sent_message = service.users().messages().send(userId=user_id, body=message).execute()
            print(f'Message Id: {sent_message["id"]}')
            return sent_message
        except Exception as e:
            print(f'An error occurred: {e}')
            return None

    # 从本地文件中加载凭据
    creds = Credentials.from_authorized_user_file(creds_file)

    # 创建 Gmail API 客户端
    service = build('gmail', 'v1', credentials=creds)

    message = create_message(to, subject, message_text)
    res = send_message(service, 'me', message)

    return json.dumps(res)
