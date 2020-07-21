const discord = require("discord.js");
const config = require("./config.json");
const fs = require("fs"); 
const bot = new discord.Client({disableEveryone: true});

bot.on("ready", async () => {
    console.log(`${bot.user.username} is ready for action!`);
    // bot.user.setActivity("Minekwaft");
});

bot.commands = new discord.Collection();
fs.readdir("./commands/", (err, files) => {
  if (err) console.error(err);
  let jsfiles = files.filter(f => f.split(".").pop() === "js");

  if (jsfiles.length <= 0) return console.log("There are no commands to load...");

  console.log(`Loading ${jsfiles.length} commands...`);
  jsfiles.forEach((f, i) => {
    let props = require(`./commands/${f}`);
    console.log(`${i + 1}: ${f} loaded!`);
    bot.commands.set(props.help.name, props);
  });
});

bot.on("message", async message =>{
    if (message.author.bot) return;
    if(message.channel.type === "dm") return;

    let prefix = config.prefix;
    let message_arr = message.content.split(" ");
    let command = message_arr[0].toLowerCase();
    let args = message_arr.slice(1);

    if (!command.startsWith(prefix)) return;
    
    let cmd = bot.commands.get(command.slice(prefix.length));
    if (cmd) cmd.run(bot, message, args);

});

bot.login(config.token);