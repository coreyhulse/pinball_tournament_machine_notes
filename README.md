## Pinball Tournament Machine Notes

## Relevant Links
* TiltForums: http://tiltforums.com/t/tournament-settings-repo-matchplay-integration/8533

## About
* The goal of this repository is to collect pinball machine settings information that would be ideal for tournament directors
* Data collected here will be ported and integrated into https://opdb.org, a public repository of pinball machine information
* Notes are being compiled by OPDB Machine Group

## Initialization
* Please drop an email to pinballspinner@gmail.com or contact Corey Hulse on http://tiltforums.com/u/coreyhulse/ to ask for access.  An Admin will add you as a Contributor.  Right now the only "Admin" is Corey so please be patient if there's a delay in access.
* You can also Fork the repo, but we'd prefer to add you directly as a contributor to the original repo.

## Naming Conventions
File names will consist of four parts in the following format: `machinename_code_id_group.md`
|field|notes|
|-|-|
|`machinename`|Name of the machine.  No Underscores or spaces.|
|`code`|Two-character code representing the type of file.<ul><li>`cs` - Competition Setup</li><li>`cn` - Competition Notes</li></ul>|
|`id`|Internal database identifier for the OPDB Group|
|`group`|OPDB Group|
|`.md`|We are using the Markdown file type|

## Workflow
* Create a branch and make your proposed changes
* File Notes:
    * 'cs' is for Competition Setup (things like software, switches, and adjustments)
    * 'cn' is for Competition Notes (things like tech notes, concerns, etc)
* Submit a pull request which will be reviewed by an Admin
* Admins will merge the pull request and manually copy the data into OPDB, which will in turn be reflected on matchplay.events.  We might have automated integration with OPDB in the future, but at the moment it's a manual copy and paste for any merge requests.

## Formatting Notes
* We are using the Markdown file type, specifically the GitHub Flavored Markdown Spec: https://github.github.com/gfm/
* All Files should be formatted with markdown where appropriate, but any plain-text contribution would be appreciated 
* For Headers, please use four hashes: `####` - this will keep the formatting clean when loading on MatchPlay.events
* Use bullets where possible as opposed to long-winded text blocks
* Use tables to organize any kind of Machine Settings / Switches; bulleted lists are also acceptable

## What is OPDB?
From https://opdb.org/about
>Every machine in the database is assigned a unique identifier. This OPDB ID is designed to convey as much information as possible in the ID itself. Each OPDB ID is made up of three parts: A mandatory group identifier followed by an optional machine identifier and an optional alias identifier. A sample OPDB ID looks like: `G43W4-MrRpw-A1B7O`:
> * `G43W4` identifies that this machine belongs to the AC/DC group of machines. The group identifier always begins with G.
> * `MrRpw` identifies that this machine is an AC/DC LE machine. The machine identifier always begins with M.
> * `A1B7O` identifies that this machines is the Back in Black variant of the AC/DC LE machine. The alias identifier always begins with an A.
> * Assigning each machine an ID consisting of these separate parts it's possible to see the relationship between machines just by examining their OPDB IDs.

## Why we are using OPDB Groups, as opposed to Machines
* It will be easier to maintain broader notes that apply to the entire group of machines, as opposed to maintaining repeated information across the same machines
* Notes about specific machines can be logged at a `Group` level
* Differences between machines regarding tournament conditions can be more easily noted and compared at the `Group` level

## Acknowledgements
* Initialization of the notes are courtesy of data pulls from:
  * PAPA/ReplayFX Competition Notes -> https://replayfoundation.org/papa/learning-center/director-guide/game-notes/
  * Dave Stewart's WA Pinball .docx Repo -> http://wapinball.net/setups/
