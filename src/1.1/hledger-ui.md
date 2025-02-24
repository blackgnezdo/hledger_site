<div class="docversions"></div>
<div class="pagetoc">
<!-- toc -->
</div>

# hledger-ui

This doc is for version **1.1**. 

## NAME

hledger-ui - curses-style interface for the hledger accounting tool

## SYNOPSIS

`hledger-ui [OPTIONS] [QUERYARGS]`\
`hledger ui -- [OPTIONS] [QUERYARGS]`

## DESCRIPTION

hledger is a cross-platform program for tracking money, time, or any
other commodity, using double-entry accounting and a simple, editable
file format. hledger is inspired by and largely compatible with
ledger(1).

hledger-ui is hledger's curses-style interface, providing an efficient
full-window text UI for viewing accounts and transactions, and some
limited data entry capability. It is easier than hledger's command-line
interface, and sometimes quicker and more convenient than the web
interface.

Like hledger, it reads data from one or more files in hledger journal,
timeclock, timedot, or CSV format specified with `-f`, or
`$LEDGER_FILE`, or `$HOME/.hledger.journal` (on windows, perhaps
`C:/Users/USER/.hledger.journal`). For more about this see hledger(1),
hledger\_journal(5) etc.

## OPTIONS

Note: if invoking hledger-ui as a hledger subcommand, write `--` before
options as shown above.

Any QUERYARGS are interpreted as a hledger search query which filters
the data.

`--watch`
:   watch for data and date changes and reload automatically

`--theme=default|terminal|greenterm`
:   use this custom display theme

`--register=ACCTREGEX`
:   start in the (first) matched account's register screen

`--change`
:   show period balances (changes) at startup instead of historical
    balances

`--flat`
:   show full account names, unindented

`-V --value`
:   show amounts as their current market value in their default
    valuation commodity (accounts screen only)

hledger general options:

`-h`
:   show general usage (or after COMMAND, the command's usage)

`--help`
:   show the current program's manual as plain text (or after an add-on
    COMMAND, the add-on's manual)

`--man`
:   show the current program's manual with man

`--info`
:   show the current program's manual with info

`--version`
:   show version

`--debug[=N]`
:   show debug output (levels 1-9, default: 1)

`-f FILE --file=FILE`
:   use a different input file. For stdin, use -

`--rules-file=RULESFILE`
:   Conversion rules file to use when reading CSV (default: FILE.rules)

`--alias=OLD=NEW`
:   display accounts named OLD as NEW

`-I --ignore-assertions`
:   ignore any failing balance assertions in the journal

hledger reporting options:

`-b --begin=DATE`
:   include postings/txns on or after this date

`-e --end=DATE`
:   include postings/txns before this date

`-D --daily`
:   multiperiod/multicolumn report by day

`-W --weekly`
:   multiperiod/multicolumn report by week

`-M --monthly`
:   multiperiod/multicolumn report by month

`-Q --quarterly`
:   multiperiod/multicolumn report by quarter

`-Y --yearly`
:   multiperiod/multicolumn report by year

`-p --period=PERIODEXP`
:   set start date, end date, and/or reporting interval all at once
    (overrides the flags above)

`--date2`
:   show, and match with -b/-e/-p/date:, secondary dates instead

`-C --cleared`
:   include only cleared postings/txns

`--pending`
:   include only pending postings/txns

`-U --uncleared`
:   include only uncleared (and pending) postings/txns

`-R --real`
:   include only non-virtual postings

`--depth=N`
:   hide accounts/postings deeper than N

`-E --empty`
:   show items with zero amount, normally hidden

`-B --cost`
:   convert amounts to their cost at transaction time (using the
    [transaction price](journal.html#transaction-prices), if any)

`--pivot TAG`
:   will transform the journal before any other processing by replacing
    the account name of every posting having the tag TAG with content
    VALUE by the account name "TAG:VALUE". The TAG will only match if it
    is a full-length match. The pivot will only happen if the TAG is on
    a posting, not if it is on the transaction. If the tag value is a
    multi:level:account:name the new account name will
    be "TAG:multi:level:account:name".

`--anon`
:   show anonymized accounts and payees

## KEYS

`?` shows a help dialog listing all keys. (Some of these also appear in
the quick help at the bottom of each screen.) Press `?` again (or
`ESCAPE`, or `LEFT`) to close it. The following keys work on most
screens:

The cursor keys navigate: `right` (or `enter`) goes deeper, `left`
returns to the previous screen,
`up`/`down`/`page up`/`page down`/`home`/`end` move up and down through
lists. Vi-style `h`/`j`/`k`/`l` movement keys are also supported. A tip:
movement speed is limited by your keyboard repeat rate, to move faster
you may want to adjust it. (If you're on a mac, the Karabiner app is one
way to do that.)

With shift pressed, the cursor keys adjust the report period, limiting
the transactions to be shown (by default, all are shown).
`shift-down/up` steps downward and upward through these standard report
period durations: year, quarter, month, week, day. Then,
`shift-left/right` moves to the previous/next period. `t` sets the
report period to today. With the `--watch` option, when viewing a
"current" period (the current day, week, month, quarter, or year), the
period will move automatically to track the current date. To set a
non-standard period, you can use `/` and a `date:` query.

`/` lets you set a general filter query limiting the data shown, using
the same [query terms](/hledger.html#queries) as in hledger and
hledger-web. While editing the query, you can use [CTRL-a/e/d/k, BS,
cursor
keys](http://hackage.haskell.org/package/brick-0.7/docs/Brick-Widgets-Edit.html#t:Editor);
press `ENTER` to set it, or `ESCAPE`to cancel. There are also keys for
quickly adjusting some common filters like account depth and
cleared/uncleared (see below). `BACKSPACE` or `DELETE` removes all
filters, showing all transactions.

`ESCAPE` removes all filters and jumps back to the top screen. Or, it
cancels a minibuffer edit or help dialog in progress.

`g` reloads from the data file(s) and updates the current screen and any
previous screens. (With large files, this could cause a noticeable
pause.)

`I` toggles balance assertion checking. Disabling balance assertions
temporarily can be useful for troubleshooting.

`a` runs command-line hledger's add command, and reloads the updated
file. This allows some basic data entry.

`E` runs \$HLEDGER\_UI\_EDITOR, or \$EDITOR, or a default
(`emacsclient -a "" -nw`) on the journal file. With some editors (emacs,
vi), the cursor will be positioned at the current transaction when
invoked from the register and transaction screens, and at the error
location (if possible) when invoked from the error screen.

`q` quits the application.

Additional screen-specific keys are described below.

## SCREENS

### Accounts screen

This is normally the first screen displayed. It lists accounts and their
balances, like hledger's balance command. By default, it shows all
accounts and their latest ending balances (including the balances of
subaccounts). if you specify a query on the command line, it shows just
the matched accounts and the balances from matched transactions.

Account names are normally indented to show the hierarchy (tree mode).
To see less detail, set a depth limit by pressing a number key, `1` to
`9`. `0` shows even less detail, collapsing all accounts to a single
total. `-` and `+` (or `=`) decrease and increase the depth limit. To
remove the depth limit, set it higher than the maximum account depth, or
press `ESCAPE`.

`F` toggles flat mode, in which accounts are shown as a flat list, with
their full names. In this mode, account balances exclude subaccounts,
except for accounts at the depth limit (as with hledger's balance
command).

`H` toggles between showing historical balances or period balances.
Historical balances (the default) are ending balances at the end of the
report period, taking into account all transactions before that date
(filtered by the filter query if any), including transactions before the
start of the report period. In other words, historical balances are what
you would see on a bank statement for that account (unless disturbed by
a filter query). Period balances ignore transactions before the report
start date, so they show the change in balance during the report period.
They are more useful eg when viewing a time log.

`C` toggles cleared mode, in which [uncleared transactions and
postings](/journal.html#transactions) are not shown. `U` toggles
uncleared mode, in which only uncleared transactions/postings are shown.

`R` toggles real mode, in which [virtual
postings](/journal.html#virtual-postings) are ignored.

`Z` toggles nonzero mode, in which only accounts with nonzero balances
are shown (hledger-ui shows zero items by default, unlike command-line
hledger).

Press `right` or `enter` to view an account's transactions register.

### Register screen

This screen shows the transactions affecting a particular account, like
a check register. Each line represents one transaction and shows:

-   the other account(s) involved, in abbreviated form. (If there are
    both real and virtual postings, it shows only the accounts affected
    by real postings.)

-   the overall change to the current account's balance; positive for an
    inflow to this account, negative for an outflow.

-   the running historical total or period total for the current
    account, after the transaction. This can be toggled with `H`.
    Similar to the accounts screen, the historical total is affected by
    transactions (filtered by the filter query) before the report start
    date, while the period total is not. If the historical total is not
    disturbed by a filter query, it will be the running historical
    balance you would see on a bank register for the current account.

If the accounts screen was in tree mode, the register screen will
include transactions from both the current account and its subaccounts.
If the accounts screen was in flat mode, and a non-depth-clipped account
was selected, the register screen will exclude transactions from
subaccounts. In other words, the register always shows the transactions
responsible for the period balance shown on the accounts screen. As on
the accounts screen, this can be toggled with `F`.

`C` toggles cleared mode, in which [uncleared transactions and
postings](/journal.html#transactions) are not shown. `U` toggles
uncleared mode, in which only uncleared transactions/postings are shown.

`R` toggles real mode, in which [virtual
postings](/journal.html#virtual-postings) are ignored.

`Z` toggles nonzero mode, in which only transactions posting a nonzero
change are shown (hledger-ui shows zero items by default, unlike
command-line hledger).

Press `right` (or `enter`) to view the selected transaction in detail.

### Transaction screen

This screen shows a single transaction, as a general journal entry,
similar to hledger's print command and journal format
(hledger\_journal(5)).

The transaction's date(s) and any cleared flag, transaction code,
description, comments, along with all of its account postings are shown.
Simple transactions have two postings, but there can be more (or in
certain cases, fewer).

`up` and `down` will step through all transactions listed in the
previous account register screen. In the title bar, the numbers in
parentheses show your position within that account register. They will
vary depending on which account register you came from (remember most
transactions appear in multiple account registers). The \#N number
preceding them is the transaction's position within the complete
unfiltered journal, which is a more stable id (at least until the next
reload).

### Error screen

This screen will appear if there is a problem, such as a parse error,
when you press g to reload. Once you have fixed the problem, press g
again to reload and resume normal operation. (Or, you can press escape
to cancel the reload attempt.)

## ENVIRONMENT

**COLUMNS** The screen width to use. Default: the full terminal width.

**LEDGER\_FILE** The journal file path when not specified with `-f`.
Default: `~/.hledger.journal` (on windows, perhaps
`C:/Users/USER/.hledger.journal`).

## FILES

Reads data from one or more files in hledger journal, timeclock,
timedot, or CSV format specified with `-f`, or `$LEDGER_FILE`, or
`$HOME/.hledger.journal` (on windows, perhaps
`C:/Users/USER/.hledger.journal`).

## BUGS

The need to precede options with `--` when invoked from hledger is
awkward.

`-f-` doesn't work (hledger-ui can't read from stdin).

`-V` affects only the accounts screen.

When you press `g`, the current and all previous screens are
regenerated, which may cause a noticeable pause with large files. Also
there is no visual indication that this is in progress.

`--watch` is not yet fully robust. It works well for normal usage, but
many file changes in a short time (eg saving the file thousands of times
with an editor macro) can cause problems at least on OSX. Symptoms
include: unresponsive UI, periodic resetting of the cursor position,
momentary display of parse errors, high CPU usage eventually subsiding,
and possibly a small but persistent build-up of CPU usage until the
program is restarted.
