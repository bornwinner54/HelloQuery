import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class DataTrain:
    def traindata(self, sentence):
        dictionary = {"Select": "select",
                      "Print": "select",
                      "View": "select",
                      "Give": "select",
                      "Display": "select",
                      "Read": "select",
                      "Show": "select",
                      "Update": "update",
                      "Modify": "update",
                      "Improve": "update",
                      "Upgrade": "update",
                      "Edit": "update",
                      "Change": "update",
                      "Insert": "insert",
                      "Enter": "insert",
                      "Add": "insert",
                      "Store": "insert",
                      "Create": "create",
                      "Build": "create",
                      "Construct": "create",
                      "Generate": "create",
                      "Truncate": "truncate",
                      "Drop": "drop",
                      "Delete": "delete",
                      "Eliminate": "delete",
                      "Rishikesh": "Rushikesh",
                      "Remove": "delete",
                      "Zap": "delete",
                      "Star": "*",
                      "All":"*",
                      "Free": "3",
                      "Tu": "2",
                      "Service":"Sarvesh",
                      "Current":"Karan",
                      "Selects": "select",
                      "Displaying": "select",
                      "Displayed": "select",
                      "Shows": "select",
                      "Shaw": "select",
                      "Showed": "select",
                      "Shown": "select",
                      "Printed": "select",
                      "Prints": "select",
                      "Prent": "select",
                      "Gives": "select",
                      "Gave": "select",
                      "Given": "select",
                      "Views": "select",
                      "Viewed": "select",
                      "Viewing": "select",
                      "Appear": "select",
                      "Appears": "select",
                      "Appeared": "select",
                      "Posted": "select",
                      "Post": "select",
                      "Posts": "select",
                      "Expose": "select",
                      "Exposed": "select",
                      "Xpose": "select",
                      "Visualize": "select",
                      "Visualise": "select",
                      "Preview": "select",
                      "Priview": "select",
                      "Proview": "select",
                      "Rid": "select",
                      "Reed": "select",
                      "Flaunt": "select",
                      "Fluent": "select",
                      "Bring": "select",
                      #            "Ring": "select",
                      "Watch": "select",
                      #            "Watches": "select",
                      "Advert": "select",
                      "Call": "select",
                      "Cal": "select",
                      "Called": "select",
                      "Calls": "select",
                      "Denote": "select",
                      "Denotes": "select",
                      #            "Donate": "select",
                      #            "Updates": "update",
                      #            "Madify": "update",
                      "Modyfy": "update",
                      "Modifi": "update",
                      "Modified": "update",
                      "Renew": "update",
                      "Rinew": "update",
                      "Revize": "update",
                      "Revyse": "update",
                      "Rivise": "update",
                      "Revised": "update",
                      "Ryvyse": "update",
                      "Revise": "update",
                      "Renovate": "update",
                      "Rinovate": "update",
                      "Rinovat": "update",
                      "Refresh": "update",
                      "Rifresh": "update",
                      "Refreshed": "update",
                      "Amand": "update",
                      "Amend": "update",
                      "Refurbish": "update",
                      "Refurbished": "update",
                      "Rejuvenate": "update",
                      "Upgraded": "update",
                      "Improved": "update",
                      "Improving": "update",
                      "Reform": "update",
                      "Reformed": "update",
                      "Repaint": "update",
                      "Repainted": "update",
                      "Edited": "update",
                      "Adjust": "update",
                      "Adjusted": "update",
                      "Addjust": "update",
                      "Correct": "update",
                      "Carrot": "update",
                      "Corrected": "update",
                      "Changed": "update",
                      "Restored": "update",
                      "Restore": "update",
                      "Inserted": "insert",
                      "Anter": "insert",
                      "Entered": "insert",
                      "Place": "insert",
                      "Ace": "insert",
                      "Placed": "insert",
                      "Fill": "insert",
                      "Feel": "insert",
                      "Feal": "insert",
                      "Fills": "insert",
                      "Filled": "insert",
                      "Imbed": "insert",
                      "Interject": "insert",
                      "Lug": "insert",
                      "Lag": "insert",
                      "Push": "insert",
                      "Pushed": "insert",
                      "Inject": "insert",
                      "Extend": "insert",
                      "Extended": "insert",
                      "Extends": "insert",
                      "Infixed": "insert",
                      "Infix": "insert",
                      "Intrude": "insert",
                      "Added": "insert",
                      "Adding": "insert",
                      "Adds": "insert",
                      "Put": "insert",
                      "Puts": "insert",
                      "Appends": "insert",
                      "Append": "insert",
                      "Paste": "insert",
                      "Attached": "insert",
                      "Attach": "insert",
                      "Join": "insert",
                      "Joined": "insert",
                      "Stored": "insert",
                      "Stores": "insert",
                      "Introduce": "insert",
                      "Introduces": "insert",
                      "Introduced": "insert",
                      "Created": "create",
                      "Creates": "create",
                      "Crate": "create",
                      "Built": "create",
                      "Make": "create",
                      "Makes": "create",
                      "Constructs": "create",
                      "Start": "create",
                      "Starts": "create",
                      "Design": "create",
                      "Designed": "create",
                      "Forge": "create",
                      "Forged": "create",
                      "Initiate": "create",
                      "Initiated": "create",
                      "Initiates": "create",
                      "Form": "create",
                      "Rom": "create",
                      "Formed": "create",
                      "Produce": "create",
                      "Produced": "create",
                      "Produces": "create",
                      "Manufacture": "create",
                      "Manifacture": "create",
                      "Manufactured": "create",
                      "Generates": "create",
                      "Generated": "create",
                      "Trincate": "truncate",
                      "Dropped": "drop",
                      "Deleted": "delete",
                      "Discard": "delete",
                      "Discarded": "delete",
                      "Discards": "delete",
                      "Dismiss": "delete",
                      "Dismissed": "delete",
                      "Extract": "delete",
                      "Extracts": "delete",
                      "Xtract": "delete",
                      "Eject": "delete",
                      "Ject": "delete",
                      "Removes": "delete",
                      "Removed": "delete",
                      "Erase": "delete",
                      "Rase": "delete",
                      "Erased": "delete",
                      "Cut": "delete",
                      "Kut": "delete",
                      "Detach": "delete",
                      "Deattach": "delete",
                      "Eliminated": "delete",
                      "Cancel": "delete",
                      "Cancelled": "delete",
                      "Clean": "delete",
                      "Lean": "delete",
                      "Cleans": "delete",
                      "Snip": "delete",
                      "Snipped": "delete",
                      "Rub": "delete",
                      "Sanitize": "delete",
                      "Sanitise": "delete",
                      "Destroy": "delete",
                      "Destroyed": "delete",
                      "Obliterate": "delete",
                      "Decontaminate": "delete",
                      "Efface": "delete",
                      "Omit": "delete",
                      "Omitted": "delete",
                      "Umit": "delete",
                      "Trim": "delete",
                      "Trimmed": "delete",
                      "Bleep": "delete",
                      "Annul": "delete",
                      "Exclude": "delete",
                      "Excludes": "delete",
                      "Xclude": "delete",
                      "Expunge": "delete",
                      "Xpunge": "delete",
                      "Squash": "delete",
                      "Quash": "delete",
                      "Sterilize": "delete",
                      "Sterilise": "delete",
                      "Abolish": "delete",
                      "Relegate": "delete",
                      "Clear": "delete",
                      "Clears": "delete",
                      "Cleared": "delete",
                      "Withdraw": "delete",
                      "Withdrawn": "delete",
                      "Withdrew": "delete",
                      "Unload": "delete",
                      "Amputate": "delete",
                      "Depose": "delete",
                      "Dethrone": "delete",
                      "Evacuate": "delete",
                      "Dislodge": "delete",
                      "Expel": "delete",
                      "Doff": "delete",
                      "Oust": "delete",
                      "Separate": "delete",
                      "Separated": "delete",
                      "Junk": "delete",
                      "Purge": "delete",
                      "Wipe": "delete",
                      "Eradicate": "delete",
                      "Undo": "delete",
                      "Repeal": "delete",
                      "Erasure": "delete",
                      "Abolition": "delete",
                      "Revoke": "delete",
                      "Demolish": "delete"
                      }
        bad_chars = ['!', '@', '#', '$', '%', '^', '&', '+', '-', '_', '/', '<', '>', '?', '|', '~']
        # example_sent = "alright # @ % * & ! Stars colors Seperated now Bring Selects me the Deletes yash vr Amend " \
        # "Star contents 18 of " \
        # "the tables name yash Tu Free "
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(sentence)
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)

        for char in bad_chars:
            for word in filtered_sentence:
                if word == char:
                    filtered_sentence.remove(char)

        count = 0
        for word in filtered_sentence:
            count = count + 1
            for meaning in dictionary:
                if word == meaning:
                    filtered_sentence[count - 1] = dictionary[word]
        return filtered_sentence