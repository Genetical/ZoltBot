# Ok, this needs needs to hold ui's and fetch the necessary data from the database
# Also, we need a database


# TODO:
# 1) Create menu templates

class ban_menu:
    ## Store template for root menu, xml version can be found in ./ui_xml_templates.txt
    @staticmethod
    def fetch_root(self):
        root_template = discord.Embed(title=":gear: Ban Menu", colour=discord.Colour(0x75ae4d))
        root_template.set_footer(text="ZoltBot by Genetical", icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/10/1040a86221334d069c8869b56be4223010c8db0e_full.jpg")

        val = "```md\n[banner](banned) <date_of_ban>: * Reason *" # Not working until a ban log is setup.
        # for ban in utils.persistence.fetch_bans(filt="recent"):
        #   val += f"\n[{ban.banner}]({ban.target}) <{ban.date}>: * {ban.reason} *"
        val += "```"
        root_template.add_field(name=":hammer:  Recent Bans", value=val)


        val = "```md\n[banner](banned) <date_of_unban>: * Reason *" # Not working until a ban log is setup.
        # for ban in utils.persistence.fetch_bans(filt="expiring"):
        #   val += f"\n[{ban.banner}]({ban.target}) <{ban.expriy}>: * {ban.reason} *"
        val += "```"
        root_template.add_field(name=":alarm_clock: Upcoming Unbans", value=val)


        root_template.add_field(name=":wrench: Commands", value="```md\n1. <View or Modify a ban>\n2. <View other Admin's bans>\n3. <View ban Statistics>\n4. <Exit the menu>```     **Type in the corresponding number to enter that menu.**")

        return root_template

    @staticmethod
    def fetch_one(self):
        one = discord.Embed(title=":gear: Ban Menu", colour=discord.Colour(0x75ae4d))
        one.set_footer(text="ZoltBot by Genetical", icon_url="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/10/1040a86221334d069c8869b56be4223010c8db0e_full.jpg")

        one.add_field(name=":file_folder: Search for a ban", value="```search [username]```", inline=False)
        one.add_field(name=":page_facing_up: View a ban", value="```view [id]  ```", inline=False)
        one.add_field(name=":wrench: Edit a ban", value="```edit [id]```", inline=False)
        one.add_field(name=":x: Exit the menu", value="```exit```", inline=False)

        return one
