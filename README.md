# pinball_td_notes

## Pinball Tournament Director Machine Notes

## About
* The goal of this repository is to collect pinball machine settings information that would be ideal for tournament directors
* Data collected here will eventually be ported and integrated into https://opdb.org, a public respository of pinball machine information
* Notes are being compiled by OPDB Group

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

## Naming Conventions
File names will consist of three parts in the following format: `machinename_code_group.md`
|field|notes|
|-|-|
|`machinename`|Name of the machine.  No Underscores or spaces.|
|`code`|Two-character code representing the type of file.<ul><li>`cs` - Competition Setup</li><li>`cn` - Competition Notes</li><li>`tg` - Tags to Add to OPDB</li></ul>|
|`group`|OPDB Group|
|`.md`|We are using the Markdown file type|

## File Format
* We are using the Markdown file type, specifically the GitHub Flavored Markdown Spec: https://github.github.com/gfm/
* All Files should be formmated with markdown where appropriate, but any plain-text contribution would be appreciated 
