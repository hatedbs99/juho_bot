#bot.py파일입니다.
import discord
from discord.ext import commands
from to import Token
import random

bot = commands.Bot(command_prefix='./')

light_nat5_moster = ['발키리', '드래곤', '피닉스', '키메라', '뱀파이어', '오라클',
                     '오컬트', '드래곤 나이트', '손오공', '아크엔젤', '신수승', '헬 레이디', '하늘 무희',
                     '선인', '극지 여왕', '해왕', '사막 여왕', '호루스', '요정왕', '웅묘 무사', '하프술사',
                     '유니콘', '드루이드', '뇌제', '데몬', '비스트 라이더', '화백', '스트라이커', '슬레이어',
                     '음양사', '마도사', '스카이 서퍼', '토템술사', '웨폰마스터']
dark_nat5_monster = ['닌자', '발키리', '드래곤', '피닉스', '키메라', '뱀파이어', '오라클',
                     '오컬트', '드래곤 나이트', '손오공', '아크엔젤', '신수승', '헬 레이디', '하늘 무희',
                     '선인', '극지 여왕', '해왕', '네오스톤 에이전트', '사막 여왕', '요정왕', '웅묘 무사', '하프술사',
                     '유니콘', '팔라딘', '드루이드', '뇌제', '데몬', '비스트 라이더', '화백', '스트라이커', '슬레이어',
                     '음양사', '요괴무사', '마도사', '스카이 서퍼', '토템술사', '웨폰마스터']
light_nat4_monster = ['구미호', '운디네', '실프', '실피드', '서큐버스', '조커', '닌자', '피에레트', '팬텀시프', '에피키온 사제',
                      '마법 궁사', '수호 나찰', '데스 나이트', '리치', '사무라이', '쿵푸걸', '브라우니 요술사', '코볼트 폭탄광',
                      '도술사', '야만왕', '해적선장', '머메이드', '마법 검사', '암살자', '네오스톤 파이터', '네오스톤 에이전트',
                      '아누비스', '잭 오 랜턴', '하그', '주사위술사', '차크람 무녀', '부메랑 전사', '드라이어드', '광전사', '스나이퍼 Mk.1',
                      '캐논걸', '가고일', '거문고 명인', '포이즌 마스터', '블레이드 댄서', '요괴무사', 'ROBO', '룬망치 대장장이']
dark_nat4_monster = ['구미호', '운디네', '실프', '실피드', '서큐버스', '조커', '피에레트', '팬텀시프',
                     '마법 궁사', '수호 나찰', '데스 나이트', '리치', '사무라이', '쿵푸걸', '브라우니 요술사', '코볼트 폭탄광',
                     '야만왕', '해적선장', '머메이드', '마법 검사', '암살자', '네오스톤 파이터', '호루스',
                     '아누비스', '잭 오 랜턴', '하그', '주사위술사', '차크람 무녀', '부메랑 전사', '드라이어드', '광전사', '스나이퍼 Mk.1',
                     '캐논걸', '가고일', '거문고 명인', '포이즌 마스터', '블레이드 댄서', '요괴무사', 'ROBO', '룬망치 대장장이']
light_nat3_monster = ['페어리', '하피', '워베어', '엘리멘탈', '가루다', '이누가미', '서펀트', '골렘', '그리폰', '인페르노', '하이엘리멘탈',
                      '하르퓨', '베어맨', '늑대인간', '아마존', '마샬캣', '방랑 기사', '바운티 헌터', '임프 챔피온', '미스틱 위치', '그림 리퍼',
                      '리빙 아머', '드렁큰 마스터', '미노타우르스', '리자드맨', '맹수 사냥꾼', '펭귄 기사', '전투 매머드', '돌격상어', '무도가', '미라',
                      '프랑켄', '엘프 순찰자']
dark_nat3_monster = ['예티', '하피', '헬하운드', '엘리멘탈', '이누가미', '서펀트', '골렘', '그리폰', '인페르노', '하이엘리멘탈',
                     '하르퓨', '베어맨', '늑대인간', '바이킹', '아마존', '마샬캣', '방랑 기사', '에피키온 사제', '임프 챔피온', '미스틱 위치', '그림 리퍼',
                     '리빙 아머', '드렁큰 마스터', '미노타우르스', '리자드맨', '도술사', '맹수 사냥꾼', '펭귄 기사', '전투 매머드', '돌격상어', '무도가', '미라',
                     '프랑켄', '하그']

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)
@bot.command(aliases=['뽑기'])
async def 빛암뽑기(ctx):
    embed = discord.Embed(title="몬스터 소환", color=0x4432a8)
    dice1 = random.random()
    dice2 = random.randint(0, 1)
    if dice2 == 0:
        light_or_dark = 'light'
    else:
        light_or_dark = 'dark'
    star = 0
    if 0 <= dice1 <= 0.0035:
        star = 5
    elif 0.0035 < dice1 <= 0.0635:
        star = 4
    else:
        star = 3

    if star == 5:
        if light_or_dark == "light":
            dice3 = random.randint(0, len(light_nat5_moster)-1)
            summoned = light_nat5_moster[dice3]
            embed.add_field(name="★★★★★", value=f"빛속성 {summoned}",inline=True)
        elif light_or_dark == "dark":
            dice3 = random.randint(0, len(dark_nat5_monster)-1)
            summoned = dark_nat5_monster[dice3]
            embed.add_field(name="★★★★★", value=f"암속성 {summoned}", inline=True)
    elif star == 4:
        if light_or_dark == "light":
            dice3 = random.randint(0, len(light_nat4_monster)-1)
            summoned = light_nat4_monster[dice3]
            embed.add_field(name="★★★★",value=f"빛속성 {summoned}",inline=True)
        elif light_or_dark == "dark":
            dice3 = random.randint(0, len(dark_nat4_monster) - 1)
            summoned = dark_nat4_monster[dice3]
            embed.add_field(name="★★★★", value=f"암속성 {summoned}", inline=True)
    elif star == 3:
        if light_or_dark == "light":
            dice3 = random.randint(0, len(light_nat3_monster) - 1)
            summoned = light_nat3_monster[dice3]
            embed.add_field(name="★★★", value=f"빛속성 {summoned}", inline=True)
        elif light_or_dark == "dark":
            dice3 = random.randint(0, len(dark_nat3_monster) - 1)
            summoned = dark_nat3_monster[dice3]
            embed.add_field(name="★★★", value=f"암속성 {summoned}", inline=True)

    await ctx.send(embed=embed)


@bot.command(aliases=['10연뽑기'])
async def 빛암뽑기10(ctx):
    embed = discord.Embed(title="몬스터 소환", color=0x4432a8)
    for _ in range(10):
        dice1 = random.random()
        dice2 = random.randint(0, 1)
        if dice2 == 0:
            light_or_dark = 'light'
        else:
            light_or_dark = 'dark'
        star = 0
        if 0 <= dice1 <= 0.0035:
            star = 5
        elif 0.0035 < dice1 <= 0.0635:
            star = 4
        else:
            star = 3

        if star == 5:
            if light_or_dark == "light":
                dice3 = random.randint(0, len(light_nat5_moster)-1)
                summoned = light_nat5_moster[dice3]
                embed.add_field(name="★★★★★", value=f"빛속성 {summoned}",inline=True)
            elif light_or_dark == "dark":
                dice3 = random.randint(0, len(dark_nat5_monster)-1)
                summoned = dark_nat5_monster[dice3]
                embed.add_field(name="★★★★★", value=f"암속성 {summoned}", inline=True)
        elif star == 4:
            if light_or_dark == "light":
                dice3 = random.randint(0, len(light_nat4_monster)-1)
                summoned = light_nat4_monster[dice3]
                embed.add_field(name="★★★★",value=f"빛속성 {summoned}",inline=True)
            elif light_or_dark == "dark":
                dice3 = random.randint(0, len(dark_nat4_monster) - 1)
                summoned = dark_nat4_monster[dice3]
                embed.add_field(name="★★★★", value=f"암속성 {summoned}", inline=True)
        elif star == 3:
            if light_or_dark == "light":
                dice3 = random.randint(0, len(light_nat3_monster) - 1)
                summoned = light_nat3_monster[dice3]
                embed.add_field(name="★★★", value=f"빛속성 {summoned}", inline=True)
            elif light_or_dark == "dark":
                dice3 = random.randint(0, len(dark_nat3_monster) - 1)
                summoned = dark_nat3_monster[dice3]
                embed.add_field(name="★★★", value=f"암속성 {summoned}", inline=True)

    await ctx.send(embed=embed)
bot.run(Token)
