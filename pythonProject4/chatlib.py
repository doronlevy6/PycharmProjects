# Protocol Constants

CMD_FIELD_LENGTH = 16  # Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4  # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10 ** LENGTH_FIELD_LENGTH - 1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
    "login_msg": "LOGIN",
    "logout_msg": "LOGOUT"
}  # .. Add more commands if needed

PROTOCOL_SERVER = {
    "login_ok_msg": "LOGIN_OK",
    "login_failed_msg": "ERROR"
}  # ..  Add more commands if needed

# Other constants

ERROR_RETURN = None  # What is returned in case of an error


def build_message(cmd, data):
    """
    Gets command name (str) and data field (str) and creates a valid protocol message
    Returns: str, or None if error occured
    """
    if len(cmd)<CMD_FIELD_LENGTH  and len(data)<MAX_DATA_LENGTH:
        full_msg =cmd+" "*(CMD_FIELD_LENGTH-len(cmd))+"|"+"0"*(4-len(str(len(data))))+str(len(data))+"|"+data
        return full_msg
    else:
        return ERROR_RETURN


def parse_message(data):
    """
    Parses protocol message and returns command name and data field
    Returns: cmd (str), data (str). If some error occured, returns None, None
    """
    # Implement code ...

    # The function should return 2 values


    if data.count("|")==2 :
        x=data.split("|")
        if all(char.isdigit() or char==" " for char in x[1]):
            t=str(int(x[1]))
            x[1]="0" * (4 - len(t)) + t
            x[0] = x[0].replace(" ", "")
            if x[1].isdigit() and int(x[1]) == len(x[2]) and int(x[1]) > 0:
                cmd=x[0]
                msg=x[2]
                return (cmd, msg)

    return ( ERROR_RETURN,ERROR_RETURN)



    return cmd, msg


def split_data(msg, expected_fields):
    """
    Helper method. gets a string and number of expected fields in it. Splits the string
    using protocol's data field delimiter (|#) and validates that there are correct number of fields.
    Returns: list of fields if all ok. If some error occured, returns None
    """
    if msg.count("#")==expected_fields:
        return msg.split("#")
    else:
        return ERROR_RETURN


def join_data(msg_fields):
    """
    Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter.
    Returns: string that looks like cell1#cell2#cell3
    """
# Implement code ...
    return "#".join(msg_fields)