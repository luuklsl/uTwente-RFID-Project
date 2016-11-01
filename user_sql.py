# -*- coding: utf-8 -*-
"""
For all your query needs to do with users!
"""

import exe_sql as sql
import random

def newUser(name,sid, hash): # user will not be created under a new name if SID already exists due to UNIQUE CONSTRAINT
    """Create a new keyhash entry, new person (pid) and link these in KPL"""
    sql.begin()
    # insert card
    sql.cur.execute("INSERT INTO key (keyhash) VALUES(?)", [hash])
    sql.commit()
    kid = sql.lastId()

    # insert user
    sql.cur.execute("INSERT INTO person (name,sid,usertype,balance) VALUES(?,?,0,?)", [name, sid,round(random.uniform(1,20),2)])
    sql.commit()
    pid = sql.lastId()

    # link user to card
    sql.cur.execute("INSERT INTO KPL (kid, pid) VALUES(?,?)", [kid, pid])
    sql.commit()
    sql.end()

def makeAdmin(pid):
    """Up someones usertype"""
    sql.begin()
    sql.cur.execute("UPDATE person SET usertype=1 WHERE pid=?", [pid])
    sql.commit()
    sql.end()

def removeAdmin(pid):
    """Down someones usertype"""
    sql.begin()
    sql.cur.execute("UPDATE person SET usertype=0 WHERE pid=?", [pid])
    sql.commit()
    sql.end()

def adminList():
    """Get list of all current admins"""
    sql.begin()
    result = sql.cur.execute("SELECT name,sid,usertype FROM person WHERE usertype=1")
    res = result.fetchall()
    sql.end()
    return res

def keyList():
    """Get list of all keys in system (mainly unreadable hashes)"""
    sql.begin()
    result = sql.cur.execute("SELECT kid, keyhash FROM key")
    res = result.fetchall()
    sql.end()
    return res

def keyUserList():
    """Get list of kid and pid in Tables"""
    sql.begin()
    result = sql.cur.execute("SELECT kid, pid FROM KPL")
    res = result.fetchall()
    sql.end()
    return res

def userList():
    """Fetch list of /normal/ users"""
    sql.begin()
    result = sql.cur.execute("SELECT pid, name, sid, balance, usertype FROM person WHERE usertype=0")
    res = result.fetchall()
    sql.end()
    return res
    
def resetUserBalance(pid):
    """Sets one users balance to 0, useful for "system clean" after invoices"""
    sql.begin()
    sql.cur.execute("UPDATE person SET balance = 0.00 where pid=?",[pid])   
    sql.commit()
    sql.end()