def reminder():
    input_ = input('don\'t read this around people, you have a message \n password?: ')
    message = ''' Hi there, you have your exams so try to think more, store your thoughts if you have any and just study more.
a one constant mind that is stable, no wipeouts no nothing

summery:
1. don't meditate make your life a meditation
2. try not to think about people, stay away from their attention except some special people
3. think more
4. store thoughts if have any
5. talk less, equavelent to 0
6. but smilke so that people would know that you are OK
7. be true be real be the more amplified verison of yourself(but the wise one's amplified).

        kindly improve the message :)
    '''

    if input_ != 'ye' and input_ !='people around me':
        return 'sucker brain, wrong password, please don\'t go hacker man on me ok. 🙇🙏'

    elif input_ == 'ye':
        print(message)
        input_ = input('how much would you rate your recent doings? : ')
        write_md_file('me_ratings.md', input_)
    write_md_file('thinkeyMode.md', '+' * 10 + message)
    input_ = input('any thought you wanna store?: ')
    write_md_file('ThinkeyThoughts', input_)

reminder()
