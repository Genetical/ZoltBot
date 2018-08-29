def wait_response(*check):
    try:
        response = await self.bot.wait_for('message', check=lambda m: m.content.split(" ")[0] in check and m.channel == ctx.channel and m.author == ctx.author, timeout=15.0)
        await response.delete()
        return response
    except asyncio.TimeoutError:
        await ctx.channel.send(':hourglass:**You took too long...**', delete_after=5.0)
        return False

done = False
while done == False:
    #Generate main menu
    await ctx.message.delete()

    embed = discord.Embed(title=":gear: Ban Menu", colour=discord.Colour(0x75ae4d), description="Manage current bans on the server")
    embed.set_footer(text="ZoltBot by Genetical", icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/10/1040a86221334d069c8869b56be4223010c8db0e_full.jpg")
    embed.add_field(name=":hammer:  Recent Bans", value="```[TIME AND DATE](BANNED USER): REASON```")
    embed.add_field(name=":alarm_clock: Upcoming Unbans", value="```[DATE OF UNBAN](BANNED USER): REASON```")
    embed.add_field(name=":wrench: Commands", value="```1 ) View or Modify a ban\n2 ) View other Admin's bans\n3 ) View ban Statistics\n4 ) Exit the menu```     **Type in the corresponding number to enter that menu.**")

    main_menu = await ctx.channel.send(embed=embed)
    response = wait_response("1","2","3","4")

    await main_menu.delete()
    if response == False:
        break


    if response == "1": # VIEW OR MODIFY A BAN
        while True:
            embed = discord.Embed(title=":gear: Ban Menu", colour=discord.Colour(0x75ae4d), description="*Directory: 1*")
            embed.set_footer(text="ZoltBot by Genetical", icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/10/1040a86221334d069c8869b56be4223010c8db0e_full.jpg")
            embed.add_field(name=":file_folder: Search for a ban", value="```search [username]```", inline=False)
            embed.add_field(name=":page_facing_up: View a ban", value="```view [id]  ```", inline=False)
            embed.add_field(name=":wrench: Edit a ban", value="```edit [id]```", inline=False)
            embed.add_field(name=":x: Exit the menu", value="```exit```", inline=False)        

            main_menu = await ctx.channel.send(embed=embed)
            response = wait_response("search","view","edit","exit")

            await main_menu.delete()
            if response == False or response.content == "exit":
                done = True
                break

            
            rlist = response.content.split(" ")
            if len(rlist) != 2:
                await ctx.channel.send(':x:**You need to have at least one argument!', delete_after=5.0)
                await asyncio.sleep(5)
                continue
            else:  
                command, arg = rlist

            if command == "search":
                #PERFORM CODE WHICH RETURNS A LIST FORMATTED AS r = [{"banid":1,"moderator":"Someguy","target":"someotherguy", "reason":"did a bad thing"},{...},...]
                r = [{"banid":1,"moderator":"Someguy","target":"someotherguy", "reason":"did a bad thing"}]
                v = "```[BANID] [MODERATOR] [TARGET] [REASON]\n"
                
                for d in r:
                    v += (f"[{d['banid']}] [{d['moderator']}] [{d['target']}] [{d['reason']}]     \n")
                v += "```"
                embed = discord.Embed(title=":gear: Ban Menu", colour=discord.Colour(0x75ae4d), description="*Directory: 1 search*")
                embed.set_footer(text="ZoltBot by Genetical", icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/10/1040a86221334d069c8869b56be4223010c8db0e_full.jpg")
                embed.add_field(name=f":mag_right: Search Result *({len(r)} results)*", value=v, inline=False)

            

        
