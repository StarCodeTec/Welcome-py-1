class pg:
    def RESULT(obj, id):
        if obj is None:
            return None
        if id == "config":
            return {"_id": obj._id, "xp_rate": obj.xp_rate, "doublexp": obj.doublexp}
        if id == "levels":
            return {"_id": obj._id, "xp": obj.xp, "levels": obj.level, "ping": obj.ping, "bg": obj.bg.strip(), "color": obj.color.strip()}
    
    
    def find(DATABASE_QUERY, DEFINED_QUERY):
        return f"SELECT * FROM {DATABASE_QUERY} WHERE {DEFINED_QUERY} = :x"


    def insert(DATABASE_QUERY=None, DEFINED_QUERY=None, preconfig=None):
        if preconfig=="config":
            return f"INSERT INTO config(_id, xp_rate, doublexp) VALUES (:_id, :xp_rate, :doublexp)"


    def GET_ALL(list, id):
        if id == "levels":
            final=[]
            for item in list:
                upsert={
                    '_id':    item._id,
                    'xp':     item.xp,
                    'levels': item.level
                }
                final.append(upsert)
            return final
